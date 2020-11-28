from GrammarType0 import GrammarType0
from GrammarType1 import GrammarType1
from TuringMachine import TuringMachine
from LBA import LBA
import argparse


def main():
    # parser = argparse.ArgumentParser(description='Correctness of multiplication expression')
    # parser.add_argument('-l', type=int, dest='left', required=True,
    #                     help='left integer in sum')
    # parser.add_argument('-r', type=int, dest='right', required=True,
    #                     help='right integer in sum')
    # parser.add_argument('--res', type=int, dest='result', required=True,
    #                     help='result integer in sum')
    # parser.add_argument('--der', dest='derivation', required=False, action='store_true',
    #                     help='get derivation')
    # parser.add_argument('--path', dest='res_path', required=False,
    #                     help='path of file where derivation will be written')
    # parser.add_argument('-t', dest='type', type=int, required=True,
    #                     help='Grammar type (0 or 1)')
    #
    # args = parser.parse_args()
    #
    # left_n = args.left
    # right_n = args.right
    # result = args.result
    # res_path = args.res_path
    # word = "".join(['1' for _ in range(left_n)] + ['*'] + ['1' for _ in range(right_n)]
    #                + ['='] + ['1' for _ in range(result)])

    tm = TuringMachine("TuringMachine.txt", "finalStates.txt")
    lba = LBA("LBA.txt", "finalStates.txt")

    grammar_t0 = GrammarType0.from_turing_m(tm)
    grammar_t1 = GrammarType1.from_lba(lba)

    res = grammar_t1.belongs("1*1=1")
    print("res")
    print(res)
    # grammar = grammar_t0 if args.type == 0 else grammar_t1
    #
    # if args.derivation is not None:
    #     if res_path is not None:
    #         with open(res_path, 'a+') as file:
    #             res = grammar.belongs(word)
    #
    #             if not res:
    #                 file.write(word + " " + str(res) + '\n')
    #                 file.write('------------------------------------\n')
    #             else:
    #                 res_sentence, consequence = res
    #                 consequence = [str(t) + '\n' for t in consequence]
    #                 file.write(word + " " + str(res_sentence) + '\n')
    #                 file.writelines(consequence)
    #                 file.write('------------------------------------\n')
    #     else:
    #         res = grammar.belongs(word)
    #         if not res:
    #             print(word, res)
    #         else:
    #             res_sentence, consequence = res
    #             print(word, res_sentence)
    #             for transition in consequence:
    #                 print(transition)
    # else:
    #     if grammar.belongs(word):
    #         print(word, True)
    #     else:
    #         print(word, False)

    return 0


if __name__ == '__main__':
    main()
