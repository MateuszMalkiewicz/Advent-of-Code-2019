from Day2.advent_day_2 import IntcodeInterpreter


class IntcodeInterpreterMk2(IntcodeInterpreter):
    def __init__(self, file_name, opcode_instructions):
        super().__init__(file_name, opcode_instructions)


opcode_day_five = {1: 'add', 2: 'multiply', 3: '', 4: '', 99: 'end'}
diagnostic_program = IntcodeInterpreterMk2('input.txt', opcode_day_five)
