def flash(octopus, octopuses):
    adjacent = get_adjacent_octopuses(octopus, octopuses)
    octopuses[octopus[1]][octopus[0]] = 0
    for (x, y) in adjacent:
        if octopuses[y][x]:
            octopuses[y][x] += 1
    return octopuses


def find_flash(octopuses):
    return [(x, y) for y in range(len(octopuses)) for x in range(len(octopuses[y])) if octopuses[y][x] > 9]


def get_adjacent_octopuses(octopus, octopuses):
    x = octopus[0]
    y = octopus[1]
    possible = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    return list(
        filter(lambda point: len(octopuses) > point[1] >= 0 and len(octopuses[point[1]]) > point[0] >= 0, possible))


def increase_level(octopuses):
    return [[octopus + 1 for octopus in row] for row in octopuses]


def main():
    f = open("input.txt", "r")
    octopuses = [[int(x) for x in line.strip()] for line in f]
    step = 1
    while True:
        octopuses = increase_level(octopuses)
        to_flash = find_flash(octopuses)
        current_step_flashes = len(to_flash)
        while to_flash:
            octopus = to_flash.pop()
            octopuses = flash(octopus, octopuses)
            if not to_flash:
                to_flash = find_flash(octopuses)
                current_step_flashes += len(to_flash)
        if current_step_flashes == len(octopuses) * len(octopuses[0]):
            all_flashed_step = step
            break
        step += 1
    print(all_flashed_step)


if __name__ == '__main__':
    main()
