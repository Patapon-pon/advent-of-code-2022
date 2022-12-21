from typing import Callable, List
from functools import reduce

addition: Callable[[int, int], int] = lambda x, y: x + y
multiplication: Callable[[int, int], int] = lambda x, y: x * y




class Monkey:
    def __init__(self, monkey_nr: int, starting_items: List[int], operation: List[str], test: List[str]) -> None:
        self.monkey_nr = monkey_nr
        self.items = starting_items
        self.operation_info = operation
        self.test = test

        self.inspected_items = 0
    
    def act(self, other_monkeys, part_one=True):
        while self.items:
            self.inspected_items += 1
            item = self.items.pop(0)
            
            operation = addition if self.operation_info[1] == "+" else multiplication
            operand_1 = item if self.operation_info[0] == "old" else int(self.operation_info[0])
            operand_2 = item if self.operation_info[2] == "old" else int(self.operation_info[2])

            if part_one: 
                item = operation(operand_1, operand_2) // 3
            else:
                item = operation(operand_1, operand_2) % worry_reducer

            divisibility_test_number = int(self.test[0].split()[-1])

            new_monkey_nr = int(self.test[1].split()[-1]) if item % divisibility_test_number == 0 else int(self.test[2].split()[-1])
            new_owner = list(filter(lambda m: m.monkey_nr == new_monkey_nr, other_monkeys))[0]
            new_owner.catch_item(item)


    def catch_item(self, item: int):
        self.items.append(item)

    def __repr__(self) -> str:
        string = f"Monkey {self.monkey_nr}:\n"
        string += f"\rHeld items: {', '.join(list(map(str, self.items)))}\n"        
        return string


def create_monkeys() -> List[Monkey]:
    monkeys = []
    with open("Day11.txt") as f:
        for line in f:
            line = line.strip("\n")
            monkey_nr = int(line[-2])
            starting_items = list(map(lambda x: int(x), f.readline().split(": ")[1].split(", ")))
            operation_line = f.readline().split("= ")[1].split()
            test_lines = [f.readline(), f.readline(), f.readline()]
            monkeys.append(Monkey(monkey_nr, starting_items, operation_line, test_lines))
            f.readline()
    return monkeys


# PART 1
monkeys = create_monkeys()
for round in range(20):
    for monkey in monkeys:
        monkey.act(list(filter(lambda m: m.monkey_nr != monkey.monkey_nr, monkeys)))

monkey_business_levels = sorted(list(map(lambda m: m.inspected_items, monkeys)), reverse=True)
print(monkey_business_levels[0] * monkey_business_levels[1])

# PART 2
monkeys = create_monkeys()
def calculate_worry_reducer(monkeys):
    """Calculate modulo with the help of chinese remainder theorem"""
    return reduce(lambda a, b: a * b, map(lambda m: int(m.test[0].split()[-1]), monkeys), 1)

worry_reducer = calculate_worry_reducer(monkeys)

for round in range(10000):
    for monkey in monkeys:
        monkey.act(list(filter(lambda m: m.monkey_nr != monkey.monkey_nr, monkeys)), False)

monkey_business_levels = sorted(list(map(lambda m: m.inspected_items, monkeys)), reverse=True)
print(monkey_business_levels[0] * monkey_business_levels[1])
