with open("puzzle-input.txt", 'r') as file:
    puzzle_input_lines = file.read()
    puzzle_input = puzzle_input_lines.splitlines()

dial_positions = [number for number in range(100)]

dial_position = 50
solution = 0

for rotation in puzzle_input:

    direction = rotation[0]
    steps = int(rotation[1:])
    dial_position = abs((dial_position + (steps if direction == "R" else -steps)) % 100)

    if dial_position == 0:
        solution += 1

print(solution)



