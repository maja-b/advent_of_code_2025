from math import prod

OPERATIONS = {'+': sum, '*': prod}

with open('day6_input.txt') as f:
    math_problems = [line for line in f.read().splitlines() if line.strip()]

*numbers_rows, operations_row = math_problems

columns = list(zip(*[row.split() for row in numbers_rows]))
operations = operations_row.split()
results = [
    OPERATIONS[sign](int(n) for n in numbers)
    for numbers, sign in zip(columns, operations)
]
print(f'Solution to Part 1 of Day 6: {sum(results)}')

columns_transposed = list(zip(*numbers_rows))

problems = []
for digits in columns_transposed:
    number = ''.join(digits).strip()
    if number == '':
        problems.append([])
    else:
        problems[-1].append(int(number)) if problems else problems.append([int(number)])

results_2 = [OPERATIONS[sign](numbers) for numbers, sign in zip(problems, operations)]
print(f'Solution to Part 2 of Day 6: {sum(results_2)}')
