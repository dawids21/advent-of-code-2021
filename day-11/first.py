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
    number_of_flashes = 0
    for step in range(100):
        octopuses = increase_level(octopuses)
        to_flash = find_flash(octopuses)
        number_of_flashes += len(to_flash)
        while to_flash:
            octopus = to_flash.pop()
            octopuses = flash(octopus, octopuses)
            if not to_flash:
                to_flash = find_flash(octopuses)
                number_of_flashes += len(to_flash)
    print(number_of_flashes)


if __name__ == '__main__':
    main()
