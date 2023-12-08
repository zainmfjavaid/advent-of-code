# Solution Runtime: 11.76ms

from collections import defaultdict

input_path = 'inputs/day_3_input.txt'
with open(input_path, 'r') as f:
    grid_lines = [line.strip('\n') for line in f.readlines()]

def find_adjacent_coords(x_coord, y_coord, grid_width, grid_height):
    adjacent_coords = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            new_x = x_coord + dx
            new_y = y_coord + dy

            if 0 <= new_x < grid_width and 0 <= new_y < grid_height:
                adjacent_coords.append((new_x, new_y))

    return adjacent_coords

grid_width = len(grid_lines[0])
grid_height = len(grid_lines)

total_sum_part1 = 0
star_positions = defaultdict(list)
total_sum_part2 = 0

for y in range(grid_height):
    x = 0
    while x < grid_width:
        if not grid_lines[y][x].isdigit():
            x += 1
            continue

        adjacent_positions = find_adjacent_coords(x, y, grid_width, grid_height)
        number_sequence = grid_lines[y][x]

        for i in range(x + 1, grid_width):
            if not grid_lines[y][i].isdigit():
                break

            number_sequence += grid_lines[y][i]
            adjacent_positions.extend(find_adjacent_coords(i, y, grid_width, grid_height))
            x += 1

        if any(grid_lines[adj_y][adj_x] != "." and not grid_lines[adj_y][adj_x].isdigit() for adj_x, adj_y in adjacent_positions):
            total_sum_part1 += int(number_sequence)

        for adj_x, adj_y in adjacent_positions:
            if grid_lines[adj_y][adj_x] == "*":
                star_positions[(adj_x, adj_y)].append(int(number_sequence))
                break

        x += 1

for numbers in star_positions.values():
    if len(numbers) > 1:
        product = 1
        for number in numbers:
            product *= number
        total_sum_part2 += product

print(f"Part 1 total sum: {total_sum_part1}")
print(f"Part 2 total sum: {total_sum_part2}")