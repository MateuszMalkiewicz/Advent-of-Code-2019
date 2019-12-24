orbit_instruction = list(map(lambda x: x.strip().split(')'), open('input.txt', 'r').readlines()))

orbits = {}
for orbit in orbit_instruction:
    orbits[orbit[1]] = orbit[0]

checksum = 0
for orbit in orbit_instruction:
    orbiting_planet = orbit[1]
    while orbiting_planet in orbits.keys():
        orbiting_planet = orbits[orbiting_planet]
        checksum += 1
print(checksum)
