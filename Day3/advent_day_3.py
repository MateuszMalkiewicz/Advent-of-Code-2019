from time import perf_counter

start_script = perf_counter()
input_file = open('input.txt', 'r')
wires_path = [line.strip().split(',') for line in input_file]
path_one_steps = wires_path[0]
path_two_steps = wires_path[1]

# path_one_steps = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
# path_two_steps = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']


def end_of_step_coordinates(start_of_step, step):
    return [start_of_step[0] + step.movement_distance()[0], start_of_step[1] + step.movement_distance()[1]]


def calculate_line_coordinates(start, end):
    if sum(start) < sum(end):
        return calculate_for_up_or_right_step(start, end)
    else:
        return calculate_for_down_or_left_step(start, end)


def calculate_for_up_or_right_step(start, end):
    if start[0] == end[0]:
        return [(start[0], start[1] + x) for x in range(1, end[1] - start[1] + 1)]
    else:
        return [(start[0] + x, start[1]) for x in range(1, end[0] - start[0] + 1)]


def calculate_for_down_or_left_step(start, end):
    if start[0] == end[0]:
        return [(end[0], end[1] + x) for x in range(start[1] - end[1])][::-1]
    else:
        return [(end[0] + x, end[1]) for x in range(start[0] - end[0])][::-1]


class Step:
    def __init__(self, step):
        self.direction = step[:1]
        self.distance = int(step[1:])
        self.is_horizontal = self.is_horizontal()
        self.direction_interpretation = {'U': [0, self.distance], 'D': [0, -self.distance],
                                         'R': [self.distance, 0], 'L': [-self.distance, 0]}

    def is_horizontal(self):
        return True if self.direction in ('R',  'L') else False

    def movement_distance(self):
        return self.direction_interpretation[self.direction]


class Path:
    def __init__(self, steps_list):
        self.starting_point = [0, 0]
        self.path_steps = steps_list
        self.vertical_paths = []
        self.horizontal_paths = []
        self.path = []
        self.path_coordinates()
        self.path_length = self.find_length_for_each_step()

    def find_length_for_each_step(self):
        path_length = []
        steps = 0
        for index in range(len(self.path)):
            path_length.append((self.path[index], steps))
            steps += 1
        return path_length

    def total_path_distance_to_point(self, other_path, crossing_point):
        total_distance = 0
        for coordinates, length in self.path_length:
            if coordinates == crossing_point:
                total_distance += length
                break
        for coordinates, length in other_path.path_length:
            if coordinates == crossing_point:
                total_distance += length
                break
        return total_distance

    def add_to_horizontal_path(self, path):
        self.horizontal_paths += path

    def add_to_vertical_path(self, path):
        self.vertical_paths += path

    def add_to_path(self, path):
        self.path += path

    def update_paths(self, start_point, end_point, step):
        if step.is_horizontal:
            self.add_to_horizontal_path(calculate_line_coordinates(start_point, end_point))
            self.add_to_path(calculate_line_coordinates(start_point, end_point))
        else:
            self.add_to_vertical_path(calculate_line_coordinates(start_point, end_point))
            self.add_to_path(calculate_line_coordinates(start_point, end_point))

    def path_coordinates(self):
        start_point = [0, 0]
        self.path.append(tuple(start_point))
        for step in self.path_steps:
            end_point = end_of_step_coordinates(start_point, step)
            self.update_paths(start_point, end_point, step)
            start_point = end_point
        self.vertical_paths = set(self.vertical_paths)
        self.horizontal_paths = set(self.horizontal_paths)

    def find_crossings(self, other_path):
        crossings = []
        for coordinates in self.horizontal_paths:
            if coordinates in other_path.vertical_paths:
                crossings.append(coordinates)
        for coordinates in self.vertical_paths:
            if coordinates in other_path.horizontal_paths:
                crossings.append(coordinates)
        return crossings


wire_one_steps = [Step(step_info) for step_info in path_one_steps]
wire_two_steps = [Step(step_info) for step_info in path_two_steps]
wire_one = Path(wire_one_steps)
wire_two = Path(wire_two_steps)
pairs = wire_one.find_crossings(wire_two)
distances = [abs(pair[0])+abs(pair[1]) for pair in pairs]

print(min(distances))

crossings_paths = []
for point in pairs:
    crossings_paths.append(wire_one.total_path_distance_to_point(wire_two, point))
print(min(crossings_paths))

print(perf_counter()-start_script)
