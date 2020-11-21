from typing import Dict, Tuple, List
from State import State
from Symbol import Symbol
from Arrow import Arrow


class TuringMachine:
    def __init__(self, name, fs_name):
        # self.transitions: Dict[Tuple[State, Symbol], Tuple[State, Symbol, Arrow]]
        self.tape_symbols = {Symbol("v"), Symbol(1), Symbol("B"), Symbol("="), Symbol("*")}
        self.alphabet = {Symbol(1), Symbol("="), Symbol("*")}
        self.start_state, self.final_states, self.transitions, self.states = TuringMachine \
            .read_transitions(name, fs_name)

    @staticmethod
    def read_transitions(cls, name, fs_name):
        res = dict()
        states = set()
        start_state = None
        final_states = set()

        with open(name, 'r') as file:
            lines = file.readlines()

            for transition_txt in lines:
                st_from, symb, _, st_to, symb_replace, direction_str = transition_txt.strip().split()
                direction = Arrow.Right if direction_str == "->" else Arrow.Left
                st_from, st_to = State(st_from), State(st_to)
                if start_state is None:
                    start_state = State(st_from)

                states.add(st_from)
                states.add(st_to)

                res[(st_from, Symbol(symb))] = (st_to, Symbol(symb_replace), direction)

        with open(fs_name, 'r') as file:
            final_states.union(set(file.readline().split()))

        return start_state, final_states, res, states

    def to_grammar_type_0(self):
        return self
