import math
from collections import Counter

CONNECTIONS_NUMBER = 1000
CIRCUITS_NUMBER = 3


def find_parent(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    parent_x, parent_y = find_parent(x), find_parent(y)
    if parent_x != parent_y:
        parents[parent_y] = parent_x


with open('day8_input.txt') as file:
    coordinates = [list(map(int, line.strip().split(','))) for line in file]

box_count = len(coordinates)
parents = list(range(box_count))
distances_ordered = sorted(
    (
        (i, j, math.dist(coordinates[i], coordinates[j]))
        for i in range(box_count)
        for j in range(i + 1, box_count)
    ),
    key=lambda x: x[2],
)

connected = set()
for box_1, box_2, _ in distances_ordered[:CONNECTIONS_NUMBER]:
    connected.add(box_1)
    connected.add(box_2)
    union(box_1, box_2)

circuit_sizes = Counter(find_parent(i) for i in connected)
largest_circuits = sorted(circuit_sizes.values(), reverse=True)[:CIRCUITS_NUMBER]
product = math.prod(largest_circuits)
print(f'Solution to Part 1 of Day 8: {product}')

disconnected = set(range(box_count)) - connected
for box_1, box_2, _ in distances_ordered[CONNECTIONS_NUMBER:]:
    disconnected.discard(box_1)
    disconnected.discard(box_2)
    if not disconnected:
        print(
            f'Solution to Part 2 of Day 8: {coordinates[box_1][0] * coordinates[box_2][0]}'
        )
        break
