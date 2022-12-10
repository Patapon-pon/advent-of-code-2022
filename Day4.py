elf_pairs = ""

with open("Day4.txt") as f:
    elf_pairs = [l.rstrip("\n") for l in f]

complete_intersections = 0
partial_intersection = 0

for pair in elf_pairs:
    elf1, elf2 = pair.split(",")
    elf1_range = elf1.split("-")
    set1 = set([a for a in range(int(elf1_range[0]), int(elf1_range[1]) + 1)])
    elf2_range = elf2.split("-")
    set2 = set([a for a in range(int(elf2_range[0]), int(elf2_range[1]) + 1)])
    if set1.issubset(set2) or set2.issubset(set1):
        complete_intersections += 1
    if len(set1.intersection(set2)) > 0:
        partial_intersection += 1


print(complete_intersections)
print(partial_intersection)