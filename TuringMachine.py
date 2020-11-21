from typing import Dict, Tuple, List
from State import State
from Symbol import Symbol
from Arrow import Arrow


class TuringMachine:
    def __init__(self, name):
        self.transitions: Dict[Tuple[State, Symbol], Tuple[State, Symbol, Arrow]] = TuringMachine.read_transitions(name)

    @staticmethod
    def read_transitions(cls, name):
        res = dict()

        with open(name, 'r') as file:
            lines = file.readlines()

            for transition_txt in lines:
                st_from, symb, _, st_to, symb_replace, direction = transition_txt.strip().split()

                res[(st_from, symb)] = (st_to, symb_replace, direction)

        return res
