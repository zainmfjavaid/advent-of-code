with open('inputs/day_4_input.txt', 'r') as f:
    cards = f.read().splitlines()
    
total_score = 0
for card in cards:
    game_info = card.split(': ')[-1]
    winning_numbers, card_numbers = game_info.split(' | ')
    winning_number_list = [int(winning_number) for winning_number in winning_numbers.split()]
    card_number_list = [int(card_number) for card_number in card_numbers.split()]
    
    # winning_number_list, card_number_list
    card_score = 0
    for winning_number in winning_number_list:
        if winning_number in card_number_list:
            card_score = (1 if card_score == 0 else card_score * 2)
    total_score += card_score
    
print(total_score)