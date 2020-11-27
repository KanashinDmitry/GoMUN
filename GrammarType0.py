from TuringMachine import TuringMachine
from Arrow import Arrow
from itertools import product
from Grammar import Grammar
from queue import Queue


class GrammarType0(Grammar):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_turing_m(cls, tm: TuringMachine):
        grammar = GrammarType0()
        grammar.tm = tm

        alphabet_with_eps = tm.alphabet.union({"eps"})

        for symbol in alphabet_with_eps:
            for tape in tm.tape_symbols:
                grammar.variables.add(f"{symbol}|{tape}")

        grammar.variables |= set([state for state in tm.states])

        grammar.variables |= {"S", "S1", "S2", "S3"}

        grammar.start_symb = "S"

        grammar.productions.append(([grammar.start_symb], ["S1", tm.start_state, "S2"]))
        for symbol in tm.alphabet:
            grammar.productions.append((["S2"], [f"{symbol}|{symbol}", "S2"]))
        grammar.productions.append((["S2"], ["S3"]))
        grammar.productions.append((["S1"], [f"eps|B"]))
        grammar.productions.append((["S3"], [f"eps|B"]))

        for state, tape_symb in product(tm.states, tm.tape_symbols):
            if (state, tape_symb) not in tm.transitions.keys():
                continue

            st_to, new_symb, direction = tm.transitions[(state, tape_symb)]

            if direction == Arrow.Right:
                for symbol in alphabet_with_eps:
                    grammar.productions.append(([state, f"{symbol}|{tape_symb}"]
                                                , [f"{symbol}|{new_symb}", st_to]))
            else:
                for symbolA, symbolB, leftSymb in product(alphabet_with_eps
                                                          , alphabet_with_eps, tm.tape_symbols):
                    grammar.productions.append(([f"{symbolB}|{leftSymb}", state, f"{symbolA}|{tape_symb}"]
                                                , [st_to, f"{symbolB}|{leftSymb}", f"{symbolA}|{new_symb}"]))

        for f_state, tape_symb, symbol in product(tm.final_states, tm.tape_symbols, alphabet_with_eps):
            grammar.productions.append(([f"{symbol}|{tape_symb}", f_state], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state, f"{symbol}|{tape_symb}"], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state], ["eps"]))

        return grammar

    def belongs(self, word: str):

        queue = Queue()

        tape = ["eps|B", "q0"] + [f'{l}|{l}' for l in word] + ["eps|B"] if self.__class__.__name__ == "GrammarType0" \
            else [f'[{self.tm.start_state}, #, {word[0]}, {word[0]}]'] + [f'[{x}, {x}]' for x in word[1:-1]] + [f'[{word[-1]}, {word[-1]}, $]']

        queue.put((tape, [(tape, None)]))
        visited_sentences = []

        while queue.qsize() > 0:
            sentence, prods_consequence = queue.get()

            sent_str = ",".join(sentence)
            if sent_str in visited_sentences:
                continue
            else:
                visited_sentences.append(sent_str)

            for prod in self.productions:
                head, body = prod
                indexes = Grammar.get_subsequence(head, sentence)
                if len(indexes) == 0:
                    continue

                if body == ['eps'] and any([symb in sentence for symb in ['1|v', '1|B', '1|1', '=|=', '*|*', 'eps|B']]):
                    continue

                for ind_start, ind_end in indexes:
                    res_part1 = [sentence[i] for i in range(ind_start)]
                    res_part2 = body
                    res_part3 = [sentence[i] for i in range(ind_end, len(sentence))]

                    new_sentence = [r for r in res_part1 + res_part2 + res_part3 if r != 'eps']
                    new_prods_consequence = prods_consequence.copy()
                    new_prods_consequence.append((new_sentence, prod))

                    queue.put((new_sentence, new_prods_consequence))

                    if "".join(new_sentence) == word or (not any([f'q{i}' in new_sentence for i in range(19) if i != 6])
                                                         and 'q6' in new_sentence):
                        return new_sentence, new_prods_consequence

        return False
