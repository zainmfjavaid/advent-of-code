# Solution Runtime: 1.83ms

with open('inputs/day_4_input.txt', 'r') as f:
    cards = f.read().splitlines()

total_score = 0
card_counts = {number:1 for number in range(1, len(cards) + 1)}
for card in cards:
    card_info, game_info = card.split(': ')
    card_number = int(card_info.split()[-1].strip())
    winning_numbers, card_numbers = game_info.split(' | ')
    winning_number_list = [int(winning_number) for winning_number in winning_numbers.split()]
    card_number_list = [int(card_number) for card_number in card_numbers.split()]
    
    card_score = 0
    match_number = 0
    for winning_number in winning_number_list:
        if winning_number in card_number_list:
            card_score = (1 if card_score == 0 else card_score * 2)
            match_number += 1
    total_score += card_score
    
    for i in range(match_number):
        if (card_number + i) < len(card_counts):
            card_counts[card_number + (i+1)] += (1*card_counts[card_number])
        
print(f'Elf Score: {total_score}')
print(f'Actual Score: {sum(card_counts.values())}')