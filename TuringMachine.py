from Machine import Machine


class TuringMachine(Machine):
    def __init__(self, name, fs_name):
        super().__init__(name, fs_name)
        self.tape_symbols = {"v", "1", "B", "=", "*"}
