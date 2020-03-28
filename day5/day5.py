input = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''

paths = list(map(lambda x: x.split(')'), open('input.txt').read().split('\n')))

# print(paths)

tree = {}
visited = set()

for i in paths:
    head = i[0]
    tail = i[1]

    if head not in tree:
        tree[head] = [tail]
        visited.add(head)
    else:
        tree[head].append(tail)

print(tree)

stack = ['COM']
count_stack = []
count = 0
total_orbs = 0
count_track = 0

while stack:

    cur_node = stack.pop()
    print(cur_node, stack, count_stack, count, total_orbs)

    if cur_node in tree:
        if len(tree[cur_node]) > 1:
            count_track = count
            count_stack.append(count_track)
        for i in tree[cur_node]:
            stack.append(i)

    else:
        if len(stack) == 0:
            break
        count = count_stack.pop()

    if len(stack) == 0:
        break

    count += 1
    total_orbs += count

print(total_orbs)
