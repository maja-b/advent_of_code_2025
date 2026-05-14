import re

with open('day2_input.txt') as file:
    scopes = file.readlines()[0].split(',')

invalid_ids_part1 = set()
invalid_ids_part2 = set()

for scope in scopes:
    scope_start, scope_end = map(int, scope.split('-'))

    for product_id in range(scope_start, scope_end + 1):
        product_id_str = str(product_id)

        if len(product_id_str) >= 2:
            match = re.match(r'^(.+)\1+$', product_id_str)
            if match:
                pattern_len = len(match.group(1))
                repetitions = len(product_id_str) // pattern_len

                invalid_ids_part2.add(product_id)
                if repetitions == 2:
                    invalid_ids_part1.add(product_id)

print(f'Solution to Part 1 of Day 2: {sum(invalid_ids_part1)}.')
print(f'Solution to Part 2 of Day 2: {sum(invalid_ids_part2)}.')
