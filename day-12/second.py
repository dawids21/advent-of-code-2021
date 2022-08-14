def create_cave_map(file_name):
    file = open(file_name, "r")
    cave_map = {}
    for line in file:
        from_cave, to_cave = line.strip().split('-')
        if from_cave not in cave_map:
            cave_map[from_cave] = []
        if to_cave not in cave_map:
            cave_map[to_cave] = []
        cave_map[from_cave].append(to_cave)
        cave_map[to_cave].append(from_cave)
    return cave_map


def is_small_cave(cave):
    return cave.islower()


def is_big_cave(cave):
    return not is_small_cave(cave)


def is_start_cave(cave):
    return cave == "start"


def is_end_cave(cave):
    return cave == "end"


def is_any_small_cave_visited_twice(path):
    return any(map(lambda x: path.count(x) == 2, filter(lambda cave: is_small_cave(cave), path)))


def find_paths(current_cave, path, cave_map):
    if is_end_cave(current_cave):
        return [path]
    if is_start_cave(current_cave):
        return []
    next_caves = cave_map[current_cave]
    paths = []
    for cave in next_caves:
        if is_small_cave(cave) and cave in path and is_any_small_cave_visited_twice(path):
            continue
        paths.extend(
            find_paths(cave, path + [cave], cave_map))
    return paths


def main():
    cave_map = create_cave_map("input.txt")
    paths = []
    for cave in cave_map["start"]:
        paths.extend(find_paths(cave, ["start", cave], cave_map))
    print(paths)
    print(len(paths))


if __name__ == '__main__':
    main()
