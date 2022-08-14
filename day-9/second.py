def get_neighbours(point, heightmap):
    neighbours = []
    if point[1] - 1 >= 0:
        neighbours.append((point[0], point[1] - 1))
    if point[0] - 1 >= 0:
        neighbours.append((point[0] - 1, point[1]))
    if point[1] + 1 < len(heightmap):
        neighbours.append((point[0], point[1] + 1))
    if point[0] + 1 < len(heightmap[point[1]]):
        neighbours.append((point[0] + 1, point[1]))
    return neighbours


def is_low_point(point, neighbours, heightmap):
    return heightmap[point[1]][point[0]] < min([heightmap[n[1]][n[0]] for n in neighbours])


def main():
    f = open("input.txt", "r")
    heightmap = [[int(x) for x in line.strip()] for line in f]
    low_points = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            point = (x, y)
            neighbours = get_neighbours(point, heightmap)
            if is_low_point(point, neighbours, heightmap):
                low_points.append(point)
    basins = []
    for low_point in low_points:
        basin = {(low_point[0], low_point[1])}
        to_visit = [low_point]
        while to_visit:
            point = to_visit.pop()
            neighbours = get_neighbours(point, heightmap)
            neighbours = [n for n in neighbours if heightmap[n[1]][n[0]] < 9]
            for neighbour in neighbours:
                if neighbour not in basin:
                    basin.add(neighbour)
                    to_visit.append(neighbour)
        basins.append(basin)
    sizes_of_basins = list(map(lambda x: len(x), basins))
    sizes_of_basins.sort()
    print(sizes_of_basins[-1] * sizes_of_basins[-2] * sizes_of_basins[-3])


if __name__ == '__main__':
    main()
