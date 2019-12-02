from math import floor

input_file = open('input.txt', 'r').readlines()
part_weights = [int(weight) for weight in input_file]

required_fuel = 0
for weight in part_weights:
    fuel = floor(weight/3) - 2
    required_fuel += fuel

print(required_fuel)

required_fuel_total = 0
for weight in part_weights:
    while floor(weight/3)-2 > 0:
        fuel = floor(weight/3) - 2
        weight = fuel
        required_fuel_total += fuel

print(required_fuel_total)
