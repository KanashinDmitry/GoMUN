from queue import Queue


class Grammar:
    def __init__(self):
        self.start_symb = None
        self.productions = []
        self.variables = set()
        self.terminals = set()
        self.tm = None

    def belongs(self, word: str):
        def get_subsequence(head, sentence):
            res = []
            if len(sentence) < len(head):
                return []
            for start_ind in range(len(sentence) - len(head) + 1):
                is_similar = True
                for head_index in range(len(head)):
                    if sentence[start_ind + head_index] != head[head_index]:
                        is_similar = False
                        break
                if is_similar:
                    res.append((start_ind, start_ind + len(head)))
            return res

        queue = Queue()

        tape = ["eps|B", "q0"] + [f'{l}|{l}' for l in word] + ["eps|B"] if self.__class__.__name__ == "GrammarType0" \
            else [f'[q19, #, {word[0]}, {word[0]}]'] + [f'[{x}, {x}]' for x in word[1:-1]] + [f'[{word[-1]}, {word[-1]}, $]']

        queue.put((tape, [(tape, None)]))
        visited_sentences = []

        while queue.qsize() > 0:
            sentence, prods_consequence = queue.get()

            sent_str = ",".join(sentence)
            if sent_str in visited_sentences:
                continue
            else:
                visited_sentences.append(sent_str)

            for prod in self.productions:
                head, body = prod
                indexes = get_subsequence(head, sentence)
                if len(indexes) == 0:
                    continue

                if body == ['eps'] and any([symb in sentence for symb in ['1|v', '1|B', '1|1', '=|=', '*|*', 'eps|B']]):
                    continue

                for ind_start, ind_end in indexes:
                    res_part1 = [sentence[i] for i in range(ind_start)]
                    res_part2 = body
                    res_part3 = [sentence[i] for i in range(ind_end, len(sentence))]

                    new_sentence = [r for r in res_part1 + res_part2 + res_part3 if r != 'eps']
                    new_prods_consequence = prods_consequence.copy()
                    new_prods_consequence.append((new_sentence, prod))

                    queue.put((new_sentence, new_prods_consequence))

                    if "".join(new_sentence) == word or (not any([f'q{i}' in new_sentence for i in range(19) if i != 6])
                                                         and 'q6' in new_sentence):
                        return new_sentence, new_prods_consequence

        return False
