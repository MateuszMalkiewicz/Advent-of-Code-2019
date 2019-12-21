password_range = list(map(lambda x: int(x), open('input.txt', 'r').readline().split('-')))


def check_if_not_decreasing(password):
    password = str(password)
    for index in range(len(password) - 1):
        if int(password[index + 1]) < int(password[index]):
            return False
    return True


def check_for_adjacent_pair(password):
    password = str(password)
    for index in range(1, len(password)):
        if password[index] == password[index-1]:
            return True
    return False


def end_of_range(position, end):
    return position == end


def find_sequences(number):
    number = str(number)
    sequence = 1
    sequences = []
    for index in range(len(number)-1):
        if number[index] == number[index+1]:
            sequence += 1
            if end_of_range(index+1, len(number)-1):
                sequences.append(sequence)
        else:
            if sequence > 1:
                sequences.append(sequence)
                sequence = 1
    return sequences if len(sequences) != 0 else [1]


def check_for_sequences_of_two(number):
    sequences = find_sequences(number)
    if 2 not in sequences:
        return False
    return True


class FindPasswords:
    def __init__(self, pass_range):
        self.pass_min_value = pass_range[0]
        self.pass_max_value = pass_range[1]
        self.passwords_amount = self.filter_passwords()

    def filter_passwords(self):
        passwords_amount = 0
        for password in range(self.pass_min_value, self.pass_max_value):
            if check_if_not_decreasing(password) and check_for_adjacent_pair(password):
                passwords_amount += 1
        return passwords_amount

    def filter_passwords_without_doubles(self):
        passwords_amount = 0
        for password in range(self.pass_min_value, self.pass_max_value):
            if check_if_not_decreasing(password) and check_for_sequences_of_two(password):
                passwords_amount += 1
        return passwords_amount


if __name__ == '__main__':
    puzzle_passwords = FindPasswords(password_range)
    print(puzzle_passwords.passwords_amount)
    print(puzzle_passwords.filter_passwords_without_doubles())
