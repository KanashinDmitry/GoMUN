from TuringMachine import TuringMachine
from Arrow import Arrow
from Symbol import *
from itertools import product


class GrammarType0:
    def __init__(self):
        self.start_symb = None
        self.productions = []
        self.variables = set()
        self.terminals = set()

    @classmethod
    def __from_turing_m(cls, tm: TuringMachine):
        grammar = GrammarType0()

        for symbol in tm.alphabet.union(Epsilon()):
            for tape in tm.tape_symbols:
                grammar.variables.add(f"{symbol}|{tape}")

        grammar.variables.union(set([state for state in tm.states]))

        grammar.variables.union({"S", "S1", "S2", "S3"})

        grammar.start_symb = "S"

        grammar.productions.append(([grammar.start_symb], ["S1", tm.start_state, "S2"]))
        for symbol in tm.alphabet:
            grammar.productions.append((["S2"], [f"{symbol}|{symbol}", "S2"]))
        grammar.productions.append((["S2"], ["S3"]))
        grammar.productions.append((["S1"], ["S1", f"{Epsilon()}|B"]))
        grammar.productions.append((["S3"], [f"{Epsilon()}|B"], "S3"))
        grammar.productions.append((["S1"], [Epsilon()]))
        grammar.productions.append((["S3"], [Epsilon()]))

        for state, tape_symb in product(tm.states, tm.tape_symbols):
            if (state, tape_symb) not in tm.transitions.keys():
                continue

            st_to, new_symb, direction = tm.transitions[(state, tape_symb)]

            if direction == Arrow.Right:
                for symbol in tm.alphabet.union(Epsilon()):
                    grammar.productions.append(([state, f"{symbol}|{tape_symb}"]
                                                , [f"{symbol}|{new_symb}", st_to]))
            else:
                for symbolA, symbolB, leftSymb in product(tm.alphabet.union(Epsilon())
                                                  , tm.alphabet.union(Epsilon()), tm.tape_symbols):
                    grammar.productions.append(([f"{symbolB}|{leftSymb}", state, f"{symbolA}|{tape_symb}"]
                                                , [st_to, f"{symbolB}|{leftSymb}", f"{symbolA}|{new_symb}"]))

        for f_state, tape_symb, symbol in product(tm.final_states, tm.tape_symbols, tm.alphabet.union(Epsilon())):
            grammar.productions.append(([f"{symbol}|{tape_symb}", f_state], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state, f"{symbol}|{tape_symb}"], [f_state, symbol, f_state]))
            grammar.productions.append(([f_state], [Epsilon()]))

        return grammar
