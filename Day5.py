from typing import List
from copy import deepcopy

class Crane:

    def __init__(self, data) -> None:
        self.crate_stacks_part1 = self.create_crate_stacks(data)
        self.crate_stacks_part2 = deepcopy(self.crate_stacks_part1)
        self.tasks = self.create_tasks(data)
    
    def create_crate_stacks(self, data: List[str]):
        rows = None
        for line in data:
            line = line.replace(" ", "")
            if line.isalnum():
                rows = len(line)
                break

        crate_stacks = [[] for _ in range(rows)]
        for line in data:

            if str.isalnum(line.replace(" ", "")):
                break

            for crate_position in range(1, len(line), 4):
                crate = line[crate_position]
                if not crate.isspace():
                    crate_stacks[crate_position // 4].append(crate)
        return crate_stacks

    def create_tasks(self, data: List[str]):
        tasks = []
        for line in data:
            if line.startswith("move"):
                tasks.append(line)
        return tasks

    def execute_tasks(self):
        for task in self.tasks:
            task_splitted = task.split(" ")

            amount = int(task_splitted[1])
            start = int(task_splitted[3]) - 1
            end = int(task_splitted[5]) - 1

            self.move_crate_part1(amount, start, end)
            self.move_crate_part2(amount, start, end)

    def move_crate_part1(self, amount, start, end):
        crates_to_move = self.crate_stacks_part1[start][:amount]
        self.crate_stacks_part1[start] = self.crate_stacks_part1[start][amount:]
        for crate in crates_to_move:
            self.crate_stacks_part1[end].insert(0, crate)

    def move_crate_part2(self, amount, start, end):
        crates_to_move = self.crate_stacks_part2[start][:amount]
        self.crate_stacks_part2[start] = self.crate_stacks_part2[start][amount:]
        for crate in crates_to_move[::-1]:
            self.crate_stacks_part2[end].insert(0, crate)


crate_input = None
with open("Day5.txt") as f:
    crate_input = [l.rstrip("\n") for l in f]

crane = Crane(crate_input)
crane.execute_tasks()

print("Part1: ", end="")
for crate_stack in crane.crate_stacks_part1:
    print(crate_stack[0], end="")
print("\nPart2: ", end="")
for crate_stack in crane.crate_stacks_part2:
    print(crate_stack[0], end="")