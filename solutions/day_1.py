# Solution Runtime: 24.65ms

input_path = 'inputs/day_1_input.txt'
with open(input_path, 'r') as f:
    bad_calibration_values = f.readlines()

digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

fixed_calibration_values = []
for bad_calibration_value in bad_calibration_values:
    numerical_characters = []
    for i in range(len(bad_calibration_value)):
        if bad_calibration_value[i].isnumeric():
            numerical_characters.append(bad_calibration_value[i])
        else:
            for digit in digits:
                if bad_calibration_value[i:].startswith(digit):
                    numerical_characters.append(digits[digit])
            
    if len(numerical_characters) >= 1:
        fixed_calibration_values.append(int(numerical_characters[0] + numerical_characters[-1]))

print(sum(fixed_calibration_values))