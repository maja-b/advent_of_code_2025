def find_max_voltage(battery_count: int, joltages: tuple[str]):
    maximum_pos = -1
    maximum_str = ''
    for i in range(battery_count, 0, -1):
        start_search = maximum_pos + 1
        end_search = len(joltages) + 1 - i
        search_list = joltages[start_search:end_search]
        maximum = max(search_list)
        maximum_pos = search_list.index(maximum) + start_search
        maximum_str += maximum
    return int(maximum_str)


maximum_joltages = []
maximum_joltages2 = []

with open('day3_input.txt') as file:
    for line in file:
        joltages = tuple(line.strip())
        maximum_joltages.append(find_max_voltage(2, joltages))
        maximum_joltages2.append(find_max_voltage(12, joltages))

print(f'Solution to Part 1 of Day 3: {sum(maximum_joltages)}.')
print(f'Solution to Part 2 of Day 3: {sum(maximum_joltages2)}.')
