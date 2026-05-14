fresh_ranges, items = [], []
with open('day5_input.txt') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if '-' in line:
            lower_bound, higher_bound = line.split('-')
            fresh_ranges.append((int(lower_bound), int(higher_bound)))
        else:
            items.append(int(line))

fresh_count = sum(
    1
    for item in items
    if any(
        lower_bound <= item <= higher_bound
        for lower_bound, higher_bound in fresh_ranges
    )
)
print(f'Solution to Part 1 of Day 5: {fresh_count}')

fresh_ranges.sort()
merged = []
for lower_bound, higher_bound in fresh_ranges:
    if merged and lower_bound <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], higher_bound))
    else:
        merged.append((lower_bound, higher_bound))

print(
    f'Solution to Part 2 of Day 5: {sum(higher_bound - lower_bound + 1 for lower_bound, higher_bound in merged)}'
)
