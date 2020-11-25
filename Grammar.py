from queue import Queue


class Grammar:
    def __init__(self):
        self.start_symb = None
        self.productions = []
        self.variables = set()
        self.terminals = set()

    def belongs(self, word: str):
        def list_contains_another(small, big):
            res = []
            if len(big) < len(small):
                return []
            for i in range(len(big) - len(small) + 1):
                for j in range(len(small)):
                    if big[i + j] != small[j]:
                        break
                else:
                    res.append((i, i + len(small)))
            return res

        queue = Queue()

        queue.put(([self.start_symb], []))

        while queue.not_empty:
            tmp, prods = queue.get()
            tmp = [t for t in tmp if t != 'eps']
            #print(f"Got {tmp, prods} from {queue}")
            for x in self.productions:
                list1, list2 = x

                indexes = list_contains_another(list1, tmp)
                if len(indexes) == 0:
                    continue

                for ind in indexes:
                    ind_start, ind_end = ind

                    res = tmp.copy()

                    res_part1 = [res[i] for i in range(ind_start)]
                    res_part2 = list2
                    res_part3 = [res[i] for i in range(ind_end, len(res))]

                    final_list = [r for r in res_part1 + res_part2 + res_part3 if r != 'eps']
                    print(f'{" ".join(tmp)} -> {final_list}')
                    prods_dup = prods.copy()
                    prods_dup.append(x)

                    queue.put((final_list, prods_dup))
                    #print(final_list)
                    if "".join(final_list) == word:
                        return prods_dup

        return False
