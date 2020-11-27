from LBA import LBA
from Arrow import Arrow
from Grammar import Grammar


class GrammarType1(Grammar):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_lba(cls, lba: LBA):
        grammar = GrammarType1()
        grammar.tm = lba

        grammar.terminals = {"1", "=", "*"}

        grammar.variables.union({"A1", "A2"})
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

        grammar.productions = unique_prod

        return grammar
