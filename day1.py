DIAL_RANGE = 100
DIAL_START = 0

dial_number = 50
start_dial = 0
start_cross_dial = 0

with open('day1_input.txt') as file:
    for instruction in file:
        instruction = int(instruction.replace('L', '-').replace('R', ''))
        multiples = abs(instruction) // DIAL_RANGE
        start_cross_dial += multiples
        if instruction < DIAL_START:
            instruction = instruction + multiples * DIAL_RANGE
        else:
            instruction = instruction - multiples * DIAL_RANGE
        if dial_number and (
            dial_number + instruction >= DIAL_RANGE
            or dial_number + instruction <= DIAL_START
        ):
            start_cross_dial += 1
        dial_number = (dial_number + instruction) % DIAL_RANGE
        if not dial_number:
            start_dial += 1

print(f'Solution to Part 1 of Day 1: {start_dial}.')
print(f'Solution to Part 2 of Day 1: {start_cross_dial}.')
