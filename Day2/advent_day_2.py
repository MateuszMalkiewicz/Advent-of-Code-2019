from numpy import prod


class IntcodeInterpreter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.intcode = self.load_file(file_name)
        self.instruction_pointer = 0
        self.opcode = {1: 'add', 2: 'multiply', 99: 'end'}
        self.instruction_length = 4

    def load_file(self, file_name):
        intcode = open(file_name, 'r').readline().split(',')
        intcode = [int(value) for value in intcode]
        return intcode

    def reset_intcode(self):
        self.intcode = self.load_file(self.file_name)
        self.instruction_pointer = 0

    def check_if_in_range(self, instruction_address):
        if instruction_address < len(self.intcode):
            return True

    def check_for_end(self):
        if self.check_if_in_range(self.instruction_pointer):
            opcode = self.opcode[self.intcode[self.instruction_pointer]]
            continue_reading = False if opcode == 'end' else True
            return continue_reading
        else:
            return False

    def find_variables_addresses(self):
        var_one_address = self.intcode[self.instruction_pointer+1]
        var_two_address = self.intcode[self.instruction_pointer+2]
        return var_one_address, var_two_address

    def find_variables(self):
        variable_addresses = self.find_variables_addresses()
        return self.intcode[variable_addresses[0]], self.intcode[variable_addresses[1]]

    def instruction_result(self):
        variables = self.find_variables()
        opcode = self.opcode[self.intcode[self.instruction_pointer]]
        if opcode == 'add':
            return sum(variables)
        elif opcode == 'multiply':
            return prod(variables)

    def result_destination(self):
        return self.intcode[self.instruction_pointer+3]

    def process_opcode(self):
        self.intcode[self.result_destination()] = self.instruction_result()

    def process_intcode(self):
        while self.check_for_end():
            self.process_opcode()
            self.instruction_pointer += self.instruction_length

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
advent_intcode.process_intcode()
advent_intcode.show_intcode()
print(advent_intcode.find_inputs_from_result(19690720))
