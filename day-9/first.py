def get_neighbours(heightmap, x, y):
    neighbours = []
    if y - 1 >= 0:
        neighbours.append(heightmap[y - 1][x])
    if x - 1 >= 0:
        neighbours.append(heightmap[y][x - 1])
    if y + 1 < len(heightmap):
        neighbours.append(heightmap[y + 1][x])
    if x + 1 < len(heightmap[y]):
        neighbours.append(heightmap[y][x + 1])
    return neighbours


def is_low_point(point, neighbours):
    return point < min(neighbours)


def main():
    f = open("input.txt", "r")
    heightmap = [[int(x) for x in line.strip()] for line in f]
    low_points = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            neighbours = get_neighbours(heightmap, x, y)
            point = heightmap[y][x]
            if is_low_point(point, neighbours):
                low_points.append(point)
    print(sum(map(lambda x: x + 1, low_points)))


if __name__ == '__main__':
    main()
