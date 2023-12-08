# Part 1 Solution Runtime: 8.84ms

with open('inputs/day_3_input.txt', 'r') as file:
    grid_lines = [line.rstrip('\n') for line in file]

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

total_sum = 0
for y in range(grid_height):
    x = 0
    while x < grid_width:
        if not grid_lines[y][x].isdigit():
            x += 1
            continue

        adjacent_checks = find_adjacent_coords(x, y, grid_width, grid_height)
        number_sequence = grid_lines[y][x]

        for i in range(x + 1, grid_width):
            if not grid_lines[y][i].isdigit():
                break

            number_sequence += grid_lines[y][i]
            adjacent_checks.extend(find_adjacent_coords(i, y, grid_width, grid_height))
            x += 1

        if any(grid_lines[adj_y][adj_x] != "." and not grid_lines[adj_y][adj_x].isdigit() for adj_x, adj_y in adjacent_checks):
            total_sum += int(number_sequence)

        x += 1

print(total_sum)