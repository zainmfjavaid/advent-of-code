# Solution Runtime: 1.06ms

input_path = 'inputs/day_2_input.txt'
with open(input_path, 'r') as f:
    games = f.readlines()
    
bag_red_count, bag_green_count, bag_blue_count = 12, 13, 14
color_count_lookup = {'red':bag_red_count, 'green':bag_green_count, 'blue':bag_blue_count}

id_sum = 0
power_sum = 0
for i, game in enumerate(games):
    is_bad_game = False
    max_color_dict = {'red':0, 'green':0, 'blue':0}
    
    draws = game.split(f'Game {i+1}: ')[-1].split('; ')
    for draw in draws:
        values = draw.split(', ')
        for value in values:
            amount, color = int(value.split()[0]), value.split()[-1].strip().strip('\n')
            
            if amount > max_color_dict[color]:
                max_color_dict[color] = amount
            if amount > color_count_lookup[color]:
                is_bad_game = True
    if not is_bad_game:
        id_sum += (i + 1)
    
    max_values = list(max_color_dict.values())
    power_sum += (max_values[0] * max_values[1] * max_values[2])

print(f'Valid game ID sum: {id_sum}')
print(f'Power sum: {power_sum}')