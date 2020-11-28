from LBA import LBA
from Arrow import Arrow
from Grammar import Grammar
from queue import Queue


class GrammarType1(Grammar):
    def __init__(self):
        super().__init__()
        self.rename_map = dict()

    @classmethod
    def from_lba(cls, lba: LBA):
        grammar = GrammarType1()
        grammar.tm = lba

        grammar.terminals = {"1", "=", "*"}

        grammar.variables.add("A1")
        grammar.variables.add("A2")
        for a in lba.alphabet:
            for x in lba.tape_symbols - {"$", "#"}:
                for q in lba.states:
                    grammar.variables.add(f"[{q}, #, {x}, {a}, $]")
                    grammar.variables.add(f"[#, {q}, {x}, {a}, $]")
                    grammar.variables.add(f"[#, {x}, {a}, {q}, $]")
                    grammar.variables.add(f"[{q}, {x}, {a}]")
                    grammar.variables.add(f"[{q}, {x}, {a}, $]")
                    grammar.variables.add(f"[{x}, {a}, {q}, $]")
                    grammar.variables.add(f"[#, {x}, {a}]")
                    grammar.variables.add(f"[{x}, {a}]")
                    grammar.variables.add(f"[{x}, {a}, $]")

        grammar.start_symb = "A1"

        for a in lba.alphabet:
            for x in lba.tape_symbols - {"$", "#"}:
                # 1
                grammar.productions.append((["A1"], [f"[{lba.start_state}, #, {a}, {a}, $]"]))

                # 2
                for key, value in lba.transitions.items():
                    key1, key2 = key
                    value1, value2, value3 = value

                    if key2 == '#' and value2 == '#' and value3 == Arrow.Right and key1 not in lba.final_states:
                        grammar.productions.append(([f"[{key1}, #, {x}, {a}, $]"], [f"[#, {value1}, {x}, {a}, $]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Left and key1 not in lba.final_states:
                        grammar.productions.append(([f"[#, {key1}, {key2}, {a}, $]"], [f"[{value1}, #, {value2}, {a}, $]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Right and key1 not in lba.final_states:
                        grammar.productions.append(([f"[#, {key1}, {key2}, {a}, $]"], [f"[#, {value2}, {a}, {value1}, $]"]))

                    if key2 == '$' and value2 == '$' and value3 == Arrow.Left and key1 not in lba.final_states:
                        grammar.productions.append(([f"[#, {x}, {a}, {key1}, $]"], [f"[#, {value1}, {x}, {a}, $]"]))

                # 3
                for q in lba.final_states:
                    grammar.productions.append(([f"[{q}, #, {x}, {a}, $]"], [a]))
                    grammar.productions.append(([f"[#, {q}, {x}, {a}, $]"], [a]))
                    grammar.productions.append(([f"[#, {x}, {a}, {q}, $]"], [a]))

                # 4
                q_start = lba.start_state
                grammar.productions.append((["A1"], [f"[{q_start}, #, {a}, {a}]", "A2"]))
                grammar.productions.append((["A2"], [f"[{a}, {a}]", "A2"]))
                grammar.productions.append((["A2"], [f"[{a}, {a}, $]"]))

                # 5
                for key, value in lba.transitions.items():
                    key1, key2 = key
                    value1, value2, value3 = value

                    if key2 == '#' and value2 == '#' and value3 == Arrow.Right and key1 not in lba.final_states:
                        grammar.productions.append(([f"[{key1}, #, {x}, {a}]"], [f"[#, {value1}, {x}, {a}]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Left and key1 not in lba.final_states:
                        grammar.productions.append(([f"[#, {key1}, {key2}, {a}]"], [f"[{value1}, #, {value2}, {a}]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Right and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[#, {key1}, {key2}, {a}]", f"[{x}, {b}]"],
                                                        [f"[#, {value2}, {a}]", f"[{value1}, {x}, {b}]"]))

                # 6
                for key, value in lba.transitions.items():
                    key1, key2 = key
                    value1, value2, value3 = value

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Right and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[{key1}, {key2}, {a}]", f"[{x}, {b}]"],
                                                        [f"[{value2}, {a}]", f"[{value1}, {x}, {b}]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Left and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[{x}, {b}]", f"[{key1}, {key2}, {a}]"],
                                                        [f"[{value1}, {x}, {b}]", f"[{value2}, {a}]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Right and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[{key1}, {key2}, {a}]", f"[{x}, {b}, $]"],
                                                        [f"[{value2}, {a}]", f"[{value1}, {x}, {b}, $]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Left and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[#, {x}, {b}]", f"[{key1}, {key2}, {a}]"],
                                                        [f"[#, {value1}, {x}, {b}]", f"[{value2}, {a}]"]))

                # 7
                for key, value in lba.transitions.items():
                    key1, key2 = key
                    value1, value2, value3 = value

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Right and key1 not in lba.final_states:
                        grammar.productions.append(([f"[{key1}, {key2}, {a}, $]"], [f"[{value2}, {a}, {value1}, $]"]))

                    if key2 == '$' and value2 == '$' and value3 == Arrow.Left and key1 not in lba.final_states:
                        grammar.productions.append(([f"[{x}, {a}, {key1}, $]"], [f"[{value1}, {x}, {a}, $]"]))

                    if key2 not in ['#', '$'] and value2 not in ['#', '$'] and value3 == Arrow.Left and key1 not in lba.final_states:
                        for b in lba.alphabet:
                            grammar.productions.append(([f"[{x}, {b}]", f"[{key1}, {key2}, {a}, $]"],
                                                        [f"[{value1}, {x}, {b}]", f"[{value2}, {a}, $]"]))

                # 8
                for q in lba.final_states:
                    grammar.productions.append(([f"[{q}, #, {x}, {a}]"], [a]))
                    grammar.productions.append(([f"[#, {q}, {x}, {a}]"], [a]))
                    grammar.productions.append(([f"[{q}, {x}, {a}]"], [a]))
                    grammar.productions.append(([f"[{q}, {x}, {a}, $]"], [a]))
                    grammar.productions.append(([f"[{x}, {a}, {q}, $]"], [a]))

                # 9
                for b in lba.alphabet:
                    grammar.productions.append(([a, f"[{x}, {b}]"], [a, b]))
                    grammar.productions.append(([a, f"[{x}, {b}, $]"], [a, b]))
                    grammar.productions.append(([f"[{x}, {a}]", b], [a, b]))
                    grammar.productions.append(([f"[#, {x}, {a}]", b], [a, b]))

        unique_prod = []
        for x in grammar.productions:
            if x not in unique_prod:
                unique_prod.append(x)

        i = 1
        for x in grammar.productions:
            part1, part2 = x
            for item in part1 + part2:
                if item[0] == "[":
                    if item not in grammar.rename_map.keys():
                        grammar.rename_map[item] = f"S{i}"
                        i += 1

        for i in range(len(grammar.productions)):
            for j in range(len(grammar.productions[i][0])):
                if grammar.productions[i][0][j][0] == "[":
                    grammar.productions[i][0][j] = grammar.rename_map[grammar.productions[i][0][j]]

            for j in range(len(grammar.productions[i][1])):
                if grammar.productions[i][1][j][0] == "[":
                    grammar.productions[i][1][j] = grammar.rename_map[grammar.productions[i][1][j]]

        grammar.productions = unique_prod

        return grammar

    def contains(self, word: str):
        queue = Queue()

        prods_list = [([self.start_symb], None)]

        prods_list.append(([self.rename_map[f"[{self.tm.start_state}, #, {word[0]}, {word[0]}]"], "A2"],
                           (["A1"], [self.rename_map[f"[{self.tm.start_state}, #, {word[0]}, {word[0]}]"], "A2"])))

        tmp_sentence = [self.rename_map[f"[{self.tm.start_state}, #, {word[0]}, {word[0]}]"], "A2"]
        for item in word[1:-1]:
            tmp_sentence = tmp_sentence[:-1] + [self.rename_map[f"[{item}, {item}]"], "A2"]
            prods_list.append((tmp_sentence,
                               (["A2"], [self.rename_map[f"[{item}, {item}]"], "A2"])))

        tmp_sentence = tmp_sentence[:-1] + [self.rename_map[f"[{word[-1]}, {word[-1]}, $]"]]
        prods_list.append((tmp_sentence,
                           (["A2"], [self.rename_map[f"[{word[-1]}, {word[-1]}, $]"]])))

        queue.put((tmp_sentence, prods_list))
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
                indexes = Grammar.get_subsequence(head, sentence)
                if len(indexes) == 0:
                    continue

                for ind_start, ind_end in indexes:
                    res_part1 = [sentence[i] for i in range(ind_start)]
                    res_part2 = body
                    res_part3 = [sentence[i] for i in range(ind_end, len(sentence))]

                    new_sentence = res_part1 + res_part2 + res_part3
                    new_prods_consequence = prods_consequence.copy()
                    new_prods_consequence.append((new_sentence, prod))

                    queue.put((new_sentence, new_prods_consequence))

                    if "".join(new_sentence) == word:
                        return new_sentence, new_prods_consequence

        return False
