INPUT_FILE = 'input.txt'
calorie_data = []
current_highest_index = 0
current_index = 0
with open(INPUT_FILE, 'r') as calorie_file:
    current_elf_calories = 0
    for line in calorie_file.readlines():
        stripped_line = line.strip()
        if stripped_line != "":
            current_elf_calories += int(stripped_line)
        else:
            calorie_data.append(current_elf_calories)
            if current_elf_calories > calorie_data[current_highest_index]:
                current_highest_index = current_index
            current_index += 1
            current_elf_calories = 0

print(current_highest_index)
print(calorie_data[current_highest_index])