intcode = list(map(lambda x: int(x), open('input.txt', 'r').readline().split(',')))


def index_of_value(index, mode):
    return intcode[index] if mode == 0 else index


def get_values(index, mode_one, mode_two):
    val_one = intcode[index_of_value(index + 1, mode_one)]
    val_two = intcode[index_of_value(index + 2, mode_two)]
    return val_one, val_two


instruction_index = 0
while instruction_index < len(intcode):
    instruction = intcode[instruction_index]
    opcode = instruction % 100
    parameter_one_mode = int(instruction / 100) % 10
    parameter_two_mode = int(instruction / 1000) % 10

    if opcode == 99:
        break

    elif opcode == 1:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        destination = intcode[instruction_index + 3]

        intcode[destination] = value_one + value_two
        instruction_index += 4

    elif opcode == 2:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        destination = intcode[instruction_index + 3]

        intcode[destination] = value_one * value_two
        instruction_index += 4

    elif opcode == 3:
        intcode[index_of_value(instruction_index+1, parameter_one_mode)] = int(input("Provide input: "))
        instruction_index += 2

    elif opcode == 4:
        print(intcode[index_of_value(instruction_index+1, parameter_one_mode)])
        instruction_index += 2

    elif opcode == 5:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        if value_one != 0:
            instruction_index = value_two
        else:
            instruction_index += 3

    elif opcode == 6:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        if value_one == 0:
            instruction_index = value_two
        else:
            instruction_index += 3

    elif opcode == 7:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        destination = intcode[instruction_index + 3]
        if value_one < value_two:
            intcode[destination] = 1
        else:
            intcode[destination] = 0
        instruction_index += 4

    elif opcode == 8:
        value_one, value_two = get_values(instruction_index, parameter_one_mode, parameter_two_mode)
        destination = intcode[instruction_index + 3]
        if value_one == value_two:
            intcode[destination] = 1
        else:
            intcode[destination] = 0
        instruction_index += 4
