lower_bound = 145852
upper_bound = 616942


def part1():
    current_num = lower_bound
    num_matches = 0
    increasing = False
    adjacent = False

    while current_num < upper_bound:
        current_arr = [x for x in str(current_num)]
        length_limit = len(current_arr)
        for i in range(0, length_limit):
            if i + 1 > length_limit - 1:
                break
            else:
                if int(current_arr[i]) <= int(current_arr[i + 1]):
                    increasing = True
                else:
                    increasing = False
                    break
                if int(current_arr[i]) == int(current_arr[i + 1]):
                    adjacent = True

        if increasing and adjacent:
            num_matches += 1
            # print('current_num: {current_num}'.format(current_num=current_num))

        current_num += 1
        increasing = False
        adjacent = False

    return num_matches


# num_matches = part1()
# print('num_matches: {num_matches}'.format(num_matches=num_matches))


def part2():
    current_num = lower_bound
    num_matches = 0
    increasing = False
    adjacent = False
    adjacency = []

    # iterate over the range
    while current_num < upper_bound:
        current_arr = [x for x in str(current_num)]
        length_limit = len(current_arr)
        i = 0
        # iterate through each digit
        while i < length_limit:
            if i + 1 > length_limit - 1:
                break
            else:
                if int(current_arr[i]) <= int(current_arr[i + 1]):
                    increasing = True
                else:
                    increasing = False
                    break
                if int(current_arr[i]) == int(current_arr[i + 1]):
                    adjacent = True
                    how_adjacent = 1
                    # iterate over the same digit and figure out adjacency
                    while i + how_adjacent < length_limit - 1 and current_arr[i] == current_arr[i + how_adjacent]:
                        # print(how_adjacent, current_arr[i], current_arr[i + how_adjacent])
                        how_adjacent += 1
                    else:
                        if current_arr[i] == current_arr[i + how_adjacent]:
                            how_adjacent += 1
                    adjacency.append(how_adjacent)
                    # print(current_arr, adjacency, i, current_arr[i], how_adjacent)
                    i = i + how_adjacent - 1
                else:
                    i += 1
        # if we have a 2 in adjacency, we're good as we only a pair of digits next to each other
        if increasing and adjacent and 2 in adjacency:
            print('match: {0}, adjacency: {1}'.format(current_arr, adjacency))
            num_matches += 1

        current_num += 1
        increasing = False
        adjacent = False
        adjacency = []
    return num_matches


num_matches = part2()
print('num_matches: {num_matches}'.format(num_matches=num_matches))
