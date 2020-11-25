from typing import Dict, Tuple, List
from Arrow import Arrow


class LBA:
    def __init__(self, name, fs_name):
        # self.transitions: Dict[Tuple[State, Symbol], Tuple[State, Symbol, Arrow]]
        self.tape_symbols = {"v", "1", "B", "=", "*", "$", "#"}
        self.alphabet = {"1", "=", "*"}
        self.start_state, self.final_states, self.transitions, self.states = LBA\
            .read_transitions(name, fs_name)

    @classmethod
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
                if start_state is None:
                    start_state = st_from

                states.add(st_from)
                states.add(st_to)

                res[(st_from, symb)] = (st_to, symb_replace, direction)

        with open(fs_name, 'r') as file:
            final_states |= set(file.readline().split())

        return start_state, final_states, res, states

    def to_grammar_type_0(self):
        return self
