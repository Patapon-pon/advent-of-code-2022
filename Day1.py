elf_calories_list = []

with open("Day1.txt") as f:
    line = f.readline()
    current_calories = 0

    while line:
        if str.isspace(line):
            elf_calories_list.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line.strip("\n"))
        
        line = f.readline()

print(max(elf_calories_list))
print(sum(sorted(elf_calories_list)[-3:]))