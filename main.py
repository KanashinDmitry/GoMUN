from GrammarType0 import GrammarType0
from GrammarType1 import GrammarType1
from TuringMachine import TuringMachine
from LBA import LBA


def main():
    tm = TuringMachine("TuringMachine.txt", "finalStates.txt")

    grammar_t0 = GrammarType0.from_turing_m(tm)
    # print(len(grammar_t0.productions))

    lba = LBA("LBA.txt", "finalStates.txt")

    grammar_t1 = GrammarType1.from_lba(lba)
    # print(len(grammar_t1.productions))

    # with open("res_grammar_1.txt", 'w+') as file:
    #     for pr in grammar_t1.productions:
    #         file.write(str(pr) + "\n")

    # with open("res_grammar_0.txt", 'w+') as file:
    #     for pr in grammar_t0.productions:
    #         file.write(str(pr) + "\n")

    # words = ["1*1=1", "111*11=111111", "11*11=1111", "11*111=111111", "111*1=111"]
    # results_t0 = []
    # results_t1 = []
    #
    # for word in words:
    #     results_t0.append(grammar_t0.belongs(word))
    #     results_t1.append(grammar_t1.belongs(word))
    #
    # with open("res_cons_t0.txt", 'a+') as file:
    #     for i in range(len(words)):
    #         file.write(f'{words[i]} - {results_t0[i][1]}\n')
    #
    # with open("res_cons_t1.txt", 'a+') as file:
    #     for i in range(len(words)):
    #         file.write(f'{words[i]} - {results_t1[i][1]}\n')

    print(grammar_t0.belongs("11*11=1111"))

    # print(grammar_t1.belongs("anything you want to check"))

    return 0


if __name__ == '__main__':
    main()
