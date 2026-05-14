def is_accessible(array: list[list[str]], row: int, col: int) -> int:
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and j >= 0:
                try:
                    if array[i][j] == '@':
                        count += 1
                except IndexError:
                    pass
        if count >= 5:
            return False
    return count < 5


def process_pass(array: list[list[str]]) -> int:
    rows, cols = len(array), len(array[0])
    to_flip = []
    for row in range(rows):
        for col in range(cols):
            if array[row][col] != '@':
                continue
            if is_accessible(array, row, col):
                to_flip.append((row, col))
    for row, col in to_flip:
        array[row][col] = 'X'
    return len(to_flip)


with open('day4_input.txt') as file:
    grid = [list(line.strip()) for line in file]

counts = []
while True:
    n = process_pass(grid)
    if n == 0:
        break
    counts.append(n)

print(f'Solution to Part 1 of Day 4: {counts[0] if counts else 0}')
print(f'Solution to Part 2 of Day 4: {sum(counts)}')
