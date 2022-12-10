import string

rucksacks = ""

with open("Day3.txt") as f:
    rucksacks = [sack.rstrip("\n") for sack in f]

ascii_priorities = {
    letter:priority + 1 for (priority, letter) in enumerate(string.ascii_letters)
}

# PART 1
priorties_sum = 0
for rucksack in rucksacks:
    midway_point = len(rucksack) // 2
    first_compartment = set(rucksack[:midway_point])
    second_compartment = set(rucksack[midway_point:])
    common_item = first_compartment.intersection(second_compartment)
    priorties_sum += ascii_priorities[common_item.pop()]

print(priorties_sum)

# PART 2
priorties_sum = 0
while len(rucksacks) > 0:
    rucksack1 = set(rucksacks.pop(0))
    rucksack2 = set(rucksacks.pop(0))
    rucksack3 = set(rucksacks.pop(0))
    common_item = rucksack1.intersection(rucksack2).intersection(rucksack3)
    priorties_sum += ascii_priorities[common_item.pop()]

print(priorties_sum)
