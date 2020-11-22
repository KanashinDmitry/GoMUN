from GrammarType0 import GrammarType0
from TuringMachine import TuringMachine


def main():
    tm = TuringMachine("TuringMachine.txt", "finalStates.txt")

    grammar = GrammarType0.from_turing_m(tm)
    print(len(grammar.productions))

    return 0


if __name__ == '__main__':
    main()
