from TuringMachine import TuringMachine
from Arrow import Arrow
from itertools import product
from Grammar import Grammar


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
