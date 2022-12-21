from queue import PriorityQueue
from string import ascii_lowercase

climb_values = { letter:height+1 for height, letter in enumerate(ascii_lowercase)}
climb_values['S'] = 1
climb_values['E'] = 26

print(climb_values)

def h(current_point, end_point):
    """
    Heuristic function that finds the distance from current position to destination.
    This function only works with A* when each step cost is 1
    """
    return abs(end_point[0] - current_point[0]) + abs(end_point[1] - current_point[1])

def get_neighbours(map, point, point_value: int):
    y, x = point

    width = len(map[y])
    height = len(map)

    neighbours = []

    # UP
    if y - 1 >= 0 and climb_values[map[y - 1][x]] - point_value <= 1:
        neighbours.append((y-1, x))

    # LEFT
    if x - 1 >= 0 and climb_values[map[y][x - 1]] - point_value <= 1:
        neighbours.append((y, x-1))

    # DOWN
    if y + 1 < height and climb_values[map[y + 1][x]] - point_value <= 1:
        neighbours.append((y+1, x))

    # RIGHT
    if x + 1 < width and climb_values[map[y][x + 1]] - point_value <= 1:
        neighbours.append((y, x+1))

    return neighbours

def get_path(start, came_from, end):
    path = None
    if end:
        path = []
        current = end
        while start not in path:
            path.append(came_from[current])
            current = came_from[current]
    return path

def a_star_search(map, start, end):
    iterations = 0

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        iterations += 1
        _, current = frontier.get()

        point_value = climb_values[map[current[0]][current[1]]]

        if current == end:
            return get_path(start, came_from, end)

        for neighbour in get_neighbours(map, current, point_value):
            new_cost = cost_so_far[current] + 1
            if neighbour not in came_from or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + h(neighbour, end)
                frontier.put((priority, neighbour))
                came_from[neighbour] = current

    # No solution...
    return None


def find_point(hill_map, point_value):
    for y in range(len(hill_map)):
        for x in range(len(hill_map[y])):
            if hill_map[y][x] == point_value:
                return y, x

def find_all_points(hill_map, point_value):
    points = set()
    for y in range(len(hill_map)):
        for x in range(len(hill_map[y])):
            if hill_map[y][x] == point_value:
                points.add((y,x))
    return points

with open("Day12.txt") as f:
    hill_map = [line.strip() for line in f]

    # PART 1
    start = find_point(hill_map, "S")
    end = find_point(hill_map, "E")

    print(len(a_star_search(hill_map, start, end)))

    # PART 2
    all_path_sizes = set()
    all_possible_starts = find_all_points(hill_map, "a")
    for a_start in all_possible_starts:
        result = a_star_search(hill_map, a_start, end)
        if result:
            all_path_sizes.add(len(result))
    
    print(min(all_path_sizes))
