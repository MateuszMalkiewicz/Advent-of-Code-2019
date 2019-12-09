from numpy import prod


class IntcodeInterpreter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.intcode = self.load_file(file_name)
        self.instruction_index = 0
        self.opcode = {1: 'add', 2: 'multiply', 99: 'end'}
        self.instruction_length = 4

    def load_file(self, file_name):
        intcode = list(map(lambda x: int(x), open(file_name, 'r').readline().split(',')))
        return intcode

    def reset_intcode(self):
        self.intcode = self.load_file(self.file_name)
        self.instruction_index = 0

    def check_if_in_range(self, instruction_address):
        if instruction_address < len(self.intcode):
            return True

    def check_for_end(self):
        if self.check_if_in_range(self.instruction_index):
            opcode = self.opcode[self.intcode[self.instruction_index]]
            continue_reading = False if opcode == 'end' else True
            return continue_reading
        else:
            return False

    def find_args_addresses(self):
        arg_one_address = self.intcode[self.instruction_index+1]
        arg_two_address = self.intcode[self.instruction_index+2]
        return arg_one_address, arg_two_address

    def find_arguments(self):
        args_addresses = self.find_args_addresses()
        return self.intcode[args_addresses[0]], self.intcode[args_addresses[1]]

    def opcode_result(self):
        arguments = self.find_arguments()
        opcode = self.opcode[self.intcode[self.instruction_index]]
        return self.opcode_interpreter(opcode, arguments)

    @staticmethod
    def opcode_interpreter(opcode, arguments):
        if opcode == 'add':
            return sum(arguments)
        elif opcode == 'multiply':
            return prod(arguments)
        else:
            pass

    def result_destination_address(self):
        return self.intcode[self.instruction_index+3]

    def process_opcode(self):
        self.intcode[self.result_destination_address()] = self.opcode_result()

    def process_intcode(self):
        while self.check_for_end():
            self.process_opcode()
            self.instruction_index += self.instruction_length

    def show_intcode(self):
        print(self.intcode)

    def change_input(self, input_one, input_two):
        self.intcode[1], self.intcode[2] = input_one, input_two

    def find_inputs_from_result(self, result):
        for input_one in range(100):
            for input_two in range(100):
                self.change_input(input_one, input_two)
                self.process_intcode()
                if self.intcode[0] == result:
                    return input_one, input_two
                self.reset_intcode()


advent_intcode = IntcodeInterpreter('input.txt')
advent_intcode.show_intcode()
advent_intcode.process_intcode()
advent_intcode.show_intcode()
print(advent_intcode.find_inputs_from_result(19690720))
