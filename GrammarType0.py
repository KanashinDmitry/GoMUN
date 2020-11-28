from TuringMachine import TuringMachine
from Arrow import Arrow
from itertools import product
from Grammar import Grammar
from queue import Queue


class GrammarType0(Grammar):
    def __init__(self):
        super().__init__()
        self.mapper_variables = dict()

    @classmethod
    def from_turing_m(cls, tm: TuringMachine):
        grammar = GrammarType0()
        grammar.tm = tm
        grammar.terminals = tm.alphabet

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
            grammar.variables.add(f"{symbol}|{symbol}")
        grammar.variables.add("eps|B")
        grammar.productions.append((["S2"], ["S3"]))
        grammar.productions.append((["S1"], ["eps|B"]))
        grammar.productions.append((["S3"], ["eps|B"]))

        for state, tape_symb in product(tm.states, tm.tape_symbols):
            if (state, tape_symb) not in tm.transitions.keys():
                continue

            st_to, new_symb, direction = tm.transitions[(state, tape_symb)]

            if direction == Arrow.Right:
                for symbol in alphabet_with_eps:
                    grammar.variables |= {f"{symbol}|{tape_symb}",  f"{symbol}|{new_symb}"}
                    grammar.productions.append(([state, f"{symbol}|{tape_symb}"]
                                                , [f"{symbol}|{new_symb}", st_to]))
            else:
                for symbolA, symbolB, leftSymb in product(alphabet_with_eps, alphabet_with_eps, tm.tape_symbols):
                    grammar.variables |= {f"{symbolB}|{leftSymb}", f"{symbolA}|{tape_symb}", f"{symbolA}|{new_symb}"}
                    grammar.productions.append(([f"{symbolB}|{leftSymb}", state, f"{symbolA}|{tape_symb}"]
                                                , [st_to, f"{symbolB}|{leftSymb}", f"{symbolA}|{new_symb}"]))

        for f_state, tape_symb, symbol in product(tm.final_states, tm.tape_symbols, alphabet_with_eps):
            grammar.variables.add(f"{symbol}|{tape_symb}")
            grammar.productions.append(([f"{symbol}|{tape_symb}", f_state], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state, f"{symbol}|{tape_symb}"], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state], ["eps"]))

        grammar.rename_variables()

        return grammar

    def rename_variables(self):
        productions = self.productions
        mapper = dict()
        index = 1
        renamed_productions = []
        start_states = ['S', 'S1', 'S2', 'S3']
        renamed_variables = set(start_states)
        states = self.tm.states

        for symb in self.variables:
            if symb not in mapper.keys():
                if symb in states:
                    mapper[symb] = symb.upper()
                elif symb == 'eps|B':
                    mapper[symb] = 'B'
                elif symb in start_states:
                    mapper[symb] = symb
                else:
                    mapper[symb] = f'V{index}'
                    index += 1

                renamed_variables.add(mapper[symb])

        for head, body in productions:
            new_prod = ([mapper[s] if s not in start_states and s in self.variables else s for s in head]
                        , [mapper[s] if s not in start_states and s in self.variables else s for s in body])
            renamed_productions.append(new_prod)

        self.variables = renamed_variables
        self.productions = renamed_productions
        self.mapper_variables = mapper

    def contains_preprocessing(self, word):
        tape, prods_consequence = (
            ['B', 'Q0', 'S2'], [(['S'], None), (['S1', 'Q0', 'S2'], (['S'], ['S1', 'Q0', 'S2']))])
        for letter in word:
            mapped_letter = self.mapper_variables[f'{letter}|{letter}']
            tape = tape[:-1] + [mapped_letter, 'S2']
            prods_consequence.append((tape, (['S2'], [mapped_letter, 'S2'])))

        tape = tape[:-1] + ['B']
        prods_consequence += [(tape[:-1] + ['S3'], (['S2'], ['S3'])), (tape, (['S3'], ['B']))]

        return tape, prods_consequence

    def contains(self, word: str):
        queue = Queue()

        tape, prods_consequence = self.contains_preprocessing(word)

        queue.put((tape, prods_consequence))
        visited_sentences = []
        final_variables = [self.mapper_variables[v] for v in ['1|v', '1|B', '1|1', '=|=', '*|*', 'eps|B']]

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

                if body == ['eps'] and any([symb in sentence for symb in final_variables]):
                    continue

                for ind_start, ind_end in indexes:

                    new_sentence = [r for r in sentence[:ind_start] + body + sentence[ind_end:] if r != 'eps']
                    new_prods_consequence = prods_consequence.copy()
                    new_prods_consequence.append((new_sentence, prod))

                    queue.put((new_sentence, new_prods_consequence))

                    if "".join(new_sentence) == word:
                        return new_sentence, new_prods_consequence

                    if (not any([f'Q{i}' in new_sentence for i in range(19) if i != 6])
                            and 'Q6' in new_sentence):
                        break

        return False
