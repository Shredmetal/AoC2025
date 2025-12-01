with open("puzzle-input.txt", 'r') as file:
    puzzle_input_lines = file.read()
    puzzle_input = puzzle_input_lines.splitlines()

dial_positions = [number for number in range(100)]

dial_position = 50
solution = 0

for rotation in puzzle_input:

    direction = rotation[0]
    steps = int(rotation[1:])

    for count in range(steps):
        dial_position = dial_position + 1 if direction == "R" else dial_position - 1
        if dial_position == -1:
            dial_position = 99
        elif dial_position == 100:
            dial_position = 0

        if dial_position == 0:
            solution += 1

print(solution)



