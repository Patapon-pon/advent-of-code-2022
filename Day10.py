current_x = 1
cycle_nr = 0
cycle_history = {cycle_nr: current_x}

instructions = []


crt_screen = [['.' for _ in range(40)] for _ in range(6)]
sprite_position = 1


with open("Day10.txt") as f:
    instructions = [l.rstrip("\n") for l in f]


while instructions:
    crt_horizontal = cycle_nr % 40
    crt_vertical = (cycle_nr - 1) // 40

    current_instruction = instructions.pop(0)
    register = current_instruction.split()
    v = None
    task = register[0]
    if len(register) == 2:
        v = int(register[1])

    sprite_in_pixel = abs(sprite_position - crt_horizontal) <= 1
    if task == "noop":
        crt_screen[crt_vertical][crt_horizontal] = '#' if sprite_in_pixel else '.'
        cycle_nr += 1
        cycle_history[cycle_nr+1] = current_x
    else:
        crt_screen[crt_vertical][crt_horizontal] = '#' if sprite_in_pixel else '.'
        cycle_nr += 1
        cycle_history[cycle_nr+1] = current_x

        crt_horizontal = cycle_nr % 40
        crt_vertical = (cycle_nr - 1) // 40
        sprite_in_pixel = abs(sprite_position - crt_horizontal) <= 1
        cycle_nr += 1
        crt_screen[crt_vertical][crt_horizontal] = '#' if sprite_in_pixel else '.'
        current_x += v
        sprite_position += v
        cycle_history[cycle_nr+1] = current_x



total_ss = 0
for cycle in range(20, 221, 40):
    total_ss += cycle_history[cycle] * cycle

print(total_ss)

for row in crt_screen:
    for cell in row:
        print(cell, end="")
    print()