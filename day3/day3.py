import math

paths = [['R8', 'U5', 'L5', 'D3'],
         ['U7', 'R6', 'D4', 'L4']]
paths = [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']]
paths = [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]

paths = list(map(lambda x: x.split(','), open('input.txt').read().split('\n')))


def get_points(path):
    print(path)
    for p in path:
        dir = p[:1]
        num = int(p[1:])
        print(dir, num)


points1 = get_points(paths[0])
points2 = get_points(paths[1])

# def part1():
#     coordinates = []
#     coord = {}
#     count = 0
#     for wire in paths:
#         # print(wire)
#         init = (0, 0)
#         min_l = math.inf
#         for ln in wire:
#             points = []
#             dir = ln[:1]
#             num = int(ln[1:])
#             # print('%s %s %s' % (ln, dir, num))
#             if dir == 'R':
#                 x = list(range(init[0] + 1, init[0] + num + 1))
#                 points = list(map(lambda z: (z, init[1]), x))
#                 init = (init[0] + num, init[1])
#             elif dir == 'L':
#                 x = list(range(init[0] - num, init[0]))
#                 points = list(map(lambda z: (z, init[1]), x))
#                 init = (init[0] - num, init[1])
#             elif dir == 'U':
#                 y = list(range(init[1] + 1, init[1] + num + 1))
#                 points = list(map(lambda z: (init[0], z), y))
#                 init = (init[0], init[1] + num)
#             elif dir == 'D':
#                 y = list(range(init[1] - num, init[1]))
#                 points = list(map(lambda z: (init[0], z), y))
#                 init = (init[0], init[1] - num)
#
#             # print(points)
#             for i in points:
#                 if i in coord and count > 0:
#                     print(i)
#                     # print('cross ln: {0}'.format(i))
#                     # print('current min: %s' % min_l)
#                     min_l = min(min_l, coord[i])
#                     print('new min: %s' % min_l)
#                 else:
#                     coord[i] = abs(i[0]) + abs(i[1])
#             # print(init)
#         count += 1
#
#     print('min_l: %s' % min_l)
#
# part1()
#
#
# import sys
#
# def calc_points_with_steps(path):
#     curx = cury = step = 0
#     directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
#     points = {}
#     for segment in path:
#         print(segment)
#         dx, dy = directions[segment[0]]
#         for _ in range(int(segment[1:])):
#             print(curx, cury)
#             curx += dx
#             cury += dy
#             step += 1
#             if (curx, cury) not in points:
#                 points[(curx, cury)] = step
#     return points
#
# # assert len(sys.argv) == 2
# wire1_path, wire2_path = open('input.txt').read().split()
# wire1_path, wire2_path = wire1_path.split(','), wire2_path.split(',')
#
# wire1_points = calc_points_with_steps(wire1_path)
# # print(wire1_points)
# wire2_points = calc_points_with_steps(wire2_path)
# # print(wire2_points)
# intersection_points = [point for point in wire1_points if point in wire2_points]
# print(intersection_points)
#
# part1 = min(abs(x) + abs(y) for (x, y) in intersection_points)
#
# print('Part 1: {0}'.format(part1))
