from GrammarType0 import GrammarType0
from GrammarType1 import GrammarType1
from TuringMachine import TuringMachine
from LBA import LBA


def main():
    tm = TuringMachine("TuringMachine.txt", "finalStates.txt")

    grammar = GrammarType0.from_turing_m(tm)
    print(len(grammar.productions))

    lba = LBA("LBA.txt", "finalStates.txt")

    grammar_t1 = GrammarType1.from_lba(lba)
    print(len(grammar_t1.productions))

    return 0


if __name__ == '__main__':
    main()
