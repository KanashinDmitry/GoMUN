from GrammarType0 import GrammarType0
from GrammarType1 import GrammarType1
from TuringMachine import TuringMachine
from LBA import LBA


def main():
    tm = TuringMachine("TuringMachine.txt", "finalStates.txt")

    grammar_t0 = GrammarType0.from_turing_m(tm)
    print(len(grammar_t0 .productions))

    #with open("res_grammar_0.txt", 'w+') as file:
    #    for pr in grammar_t0.productions:
    #        file.write(str(pr) + "\n")

    words = ["1*1=1", "111*11=111111", "11*11=1111", "11*111=111111", "111*1=111"]
    incorrect_words = ["1*1=11", "111*1=1", "11*111=1111111111111"]
    results_t0 = []

    for index, word in enumerate(words[1:2]):
        #print(word, grammar_t0.accepts(word))
        results_t0.append(grammar_t0.belongs(word))
        #print(f'{word}, {results_t0[index]}')
        with open("res_cons_t0.txt", 'a+') as file:
            file.write(f'{word}, {results_t0[index]}\n')

    lba = LBA("LBA.txt", "finalStates.txt")

    grammar_t1 = GrammarType1.from_lba(lba)
    print(len(grammar_t1.productions))

    #print(grammar_t1.belongs("1*1=1"))

    return 0


if __name__ == '__main__':
    main()
