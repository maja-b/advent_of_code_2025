with open('day7_input.txt') as file:
    manifold = [list(line.strip()) for line in file]

first_row = manifold[0]
start = next(
    (index for index, character in enumerate(first_row) if character == 'S'), None
)
if start is None:
    raise ValueError('Start index not found.')

beam_indices = {start}
timelines = {start: 1}
split_count = 0

for row in manifold[1:]:
    new_beam_indices = []
    width = len(row)
    for index in beam_indices:
        character = row[index]
        if character == '.':
            row[index] = '|'
            new_beam_indices.append(index)
        elif character == '^':
            split_count += 1
            index_timelines = timelines[index]
            timelines[index] = 0
            if index - 1 >= 0:
                row[index - 1] = '|'
                new_beam_indices.append(index - 1)
                timelines[index - 1] = timelines.get(index - 1, 0) + index_timelines
            if index + 1 < width:
                row[index + 1] = '|'
                new_beam_indices.append(index + 1)
                timelines[index + 1] = timelines.get(index + 1, 0) + index_timelines
    beam_indices = set(new_beam_indices)

print(f'Solution to Part 1 of Day 7: {split_count}')
print(f'Solution to Part 2 of Day 7: {sum(timelines.values())}')
