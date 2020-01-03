import functools

fuels = []

with open('input.txt') as file:
    opcode = file.readlines()


def part1():

    # initialize values
    opcode_arr = [int(ele) for ele in opcode[0].split(',')]
    idx = 0
    code = opcode_arr[idx]
    opcode_arr[1] = 12
    opcode_arr[2] = 2

    while code != 99:

        # add
        if code == 1:
            opcode_arr[opcode_arr[idx + 3]] = opcode_arr[opcode_arr[idx + 1]] + opcode_arr[opcode_arr[idx + 2]]
        # multiply
        elif code == 2:
            opcode_arr[opcode_arr[idx + 3]] = opcode_arr[opcode_arr[idx + 1]] * opcode_arr[opcode_arr[idx + 2]]
        idx = idx + 4
        code = opcode_arr[idx]

    print('part1: %s' % opcode_arr[0])


part1()


def part2():
    arr_1 = range(1, 100)
    arr_2 = range(1, 100)

    # iterate over a range of values for the inputs instead of 12 and 2
    for noun in arr_1:
        for verb in arr_2:
            opcode_arr = [int(ele) for ele in opcode[0].split(',')]
            idx = 0
            code = opcode_arr[idx]
            opcode_arr[1] = noun
            opcode_arr[2] = verb

            while code != 99:

                # add
                if code == 1:
                    opcode_arr[opcode_arr[idx + 3]] = opcode_arr[opcode_arr[idx + 1]] + opcode_arr[opcode_arr[idx + 2]]
                # multiply
                elif code == 2:
                    opcode_arr[opcode_arr[idx + 3]] = opcode_arr[opcode_arr[idx + 1]] * opcode_arr[opcode_arr[idx + 2]]
                idx = idx + 4
                code = opcode_arr[idx]

            # exit condition
            if opcode_arr[0] == 19690720:
                print('_arr: %s' % opcode_arr)
                print('part2: %s' % (100 * noun + verb))


part2()
