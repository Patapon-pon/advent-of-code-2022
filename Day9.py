from typing import Tuple


class Head:
    
    def __init__(self) -> None:
        self.location = [0, 0] # Start
        self.movement_map = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    
    def move(self, direction: str) -> None:
        move_y, move_x = self.movement_map[direction]
        self.location[0] = self.location[0] + move_y
        self.location[1] = self.location[1] + move_x

class Tail:
    
    def __init__(self, head: Head) -> None:
        self.head = head
        self.location = [0, 0] # Start
        self.visited_locations = {(0, 0)}

        self.possible_movements = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def get_move(self) -> Tuple[int, int]:
        # Get y and x distance from head
        head_y, head_x = self.head.location

        distance_y = self.location[0] - head_y
        distance_x = self.location[1] - head_x

        # Don't move if setup is this: HT (no space between head and tail)
        if (abs(distance_y) == 1 and abs(distance_x) == 1) or (abs(distance_y) == 1 and distance_x == 0) or (distance_y == 0 and abs(distance_x) == 1) or (distance_x == 0 and distance_y == 0):
            #print("Stood still")
            return (0, 0)

        chosen_move = (0, 0)
        for move in self.possible_movements:
            move_distance_y = abs(distance_y + move[0])
            move_distance_x = abs(distance_x + move[1])

            if (move_distance_y == 1 and move_distance_x == 0) or (move_distance_y == 0 and move_distance_x == 1):
                chosen_move = move
            
            # diagonal movement
            if (abs(distance_y) == 2 and abs(distance_x) == 2 and move_distance_y == 1 and move_distance_x == 1):
                chosen_move = move
        
        #print(f"Chosen move: {chosen_move}")
        return chosen_move

    def move(self) -> None:
        move_y, move_x = self.get_move()
        self.location[0] = self.location[0] + move_y
        self.location[1] = self.location[1] + move_x
        self.visited_locations.add(tuple(self.location))

with open("Day9.txt") as f:
    instructions = [l.rstrip("\n") for l in f]

head_part1 = Head()
tail_part1 = Tail(head_part1)

last_tail = None
prev_tail = None
head_part2 = Head()
tails_part2 = []

for tail in range(9):
    if prev_tail == None:
        prev_tail = Tail(head_part2)
        tails_part2.append(prev_tail)
    else:
        next_tail = Tail(prev_tail)
        prev_tail = next_tail
        tails_part2.append(prev_tail)
    
    if tail == 8:
        last_tail = prev_tail
    
for instruction in instructions:
    direction, steps = instruction.split(" ")
    for _ in range(int(steps)):
        head_part1.move(direction)
        tail_part1.move()
        #print(f"Head location: {head.location}")
        #print(f"Tail location: {tail.location}")

for instruction in instructions:
    direction, steps = instruction.split(" ")
    for _ in range(int(steps)):
        head_part2.move(direction)
        #print(f"Head location: {head_part2.location}")
        for i, tail in enumerate(tails_part2):
            tail.move()
            #print(f"Tail nr.{i+1} location: {tail.location}")

#print(sorted(list(tail.visited_locations)))
#print(len(tail_part1.visited_locations))
print(len(last_tail.visited_locations))

"""
max_y = max(tail.visited_locations, key=lambda p: p[0])[0]
min_y = min(tail.visited_locations, key=lambda p: p[0])[0]

max_x = max(tail.visited_locations, key=lambda p: p[1])[1]
min_x = min(tail.visited_locations, key=lambda p: p[1])[1]

# draw map
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (y, x) == (0, 0):
            print("s", end="")
        elif (y, x) == tuple(tail.location):
            print("T", end="")
        elif (y, x) == tuple(head.location):
            print("H", end="")
        elif (y, x) in tail.visited_locations:
            print("#", end="")
        else:
            print(".", end="")
    print()
"""