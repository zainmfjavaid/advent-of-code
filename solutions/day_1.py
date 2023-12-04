input_path = 'inputs/day_1_input.txt'
with open(input_path, 'r') as f:
    bad_calibration_values = f.readlines()

fixed_calibration_values = []
for bad_calibration_value in bad_calibration_values:
    numerical_characters = [char for char in bad_calibration_value if char.isnumeric()]
    if len(numerical_characters) >= 1:
        fixed_calibration_values.append(int(numerical_characters[0] + numerical_characters[-1]))

print(sum(fixed_calibration_values))