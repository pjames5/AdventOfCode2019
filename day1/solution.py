import functools

fuels = []

masses = list(map(int, open('input.txt').readlines()))


# fuel calculation function
def calculate_fuel(mass):
    return (int(mass) // 3) - 2


# part 1 - iterate over inputs and calculate mass, add all together
def part1():
    for mass in masses:
        fuels.append(calculate_fuel(mass))

    return functools.reduce(lambda a, b: a + b, fuels)


# iterate for a single module
def part2(m):
    part2_sum = 0
    res = calculate_fuel(m)
    while res > 0:
        part2_sum += res
        res = calculate_fuel(res)
    return int(part2_sum)


fuel_sum_2 = 0
for mass in masses:
    fuel_sum = part2(mass)
    fuel_sum_2 += fuel_sum

print('part1: %s' % part1())
print('part2: %s' % fuel_sum_2)
