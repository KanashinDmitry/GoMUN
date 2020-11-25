from queue import Queue


class Grammar:
    def __init__(self):
        self.start_symb = None
        self.productions = []
        self.variables = set()
        self.terminals = set()

    def belongs(self, word: str):
        def list_contains_another(small, big):
            if len(big) < len(small):
                return False
            for i in range(len(big) - len(small) + 1):
                for j in range(len(small)):
                    if big[i + j] != small[j]:
                        break
                else:
                    return i, i + len(small)
            return False

        def dup_list(lst):
            result = []

            for item in lst:
                result.append(item)

            return result

        def convert_list_to_word(lst):
            converted_word = ""
            for l in lst:
                converted_word += l

            return converted_word

        queue = Queue()

        queue.put(([self.start_symb], []))

        while queue.not_empty:
            tmp, prods = queue.get()
            tmp = [t for t in tmp if t != 'eps']
            #print(f"Got {tmp, prods} from {queue}")
            for x in self.productions:
                list1, list2 = x
                indexes = list_contains_another(list1, tmp)
                if not indexes:
                    continue

                ind_start, ind_end = indexes

                res = dup_list(tmp)

                res_part1 = [res[i] for i in range(ind_start)]
                res_part2 = list2
                res_part3 = [res[i] for i in range(ind_end, len(res))]

                final_list = [r for r in res_part1 + res_part2 + res_part3 if r != 'eps']
                print(f'{" ".join(tmp)} -> {final_list}')
                prods_dup = prods.copy()
                prods_dup.append(x)

                queue.put((final_list, prods_dup))
                #print(final_list)
                if convert_list_to_word(final_list) == word:
                    return prods_dup

        return False
