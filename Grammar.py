class Grammar:
    def __init__(self):
        self.start_symb = None
        self.productions = []
        self.variables = set()
        self.terminals = set()
        self.tm = None

    @staticmethod
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

    def contains(self, word: str):
        pass
