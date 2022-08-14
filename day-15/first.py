import heapq

MAX_INT = 99999


def find_successors(cavern_map):
    successors = {}
    for y in range(len(cavern_map)):
        for x in range(len(cavern_map[y])):
            current = []
            if y - 1 >= 0:
                current.append((x, y - 1))
            if x - 1 >= 0:
                current.append((x - 1, y))
            if y + 1 < len(cavern_map):
                current.append((x, y + 1))
            if x + 1 < len(cavern_map[y]):
                current.append((x + 1, y))
            successors[(x, y)] = current

    return successors


def extend_cavern_map(cavern_map):
    for i in range(1, 5):
        for j in range(len(cavern_map)):
            cavern_map[j].extend(list(map(lambda x: (x + i - 1) % 9 + 1, cavern_map[j][:num_of_columns])))
    for i in range(1, 5):
        cavern_map.extend([(x + i - 1) % 9 + 1 for x in row] for row in cavern_map[:num_of_rows])


def main():
    file = open("input.txt", "r")
    cavern_map = [[int(x) for x in line.strip()] for line in file]
    num_of_rows = len(cavern_map)
    num_of_columns = len(cavern_map[0])
    extend_cavern_map(cavern_map)

    distances = [[MAX_INT for _ in range(num_of_columns)] for _ in range(num_of_rows)]
    distances[0][0] = 0
    successors = find_successors(cavern_map)
    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    while heap:
        current = heapq.heappop(heap)[1]
        for v in successors[current]:
            new_distance = distances[v[1]][v[0]]
            if new_distance > distances[current[1]][current[0]] + cavern_map[v[1]][v[0]]:
                if new_distance != MAX_INT:
                    heap.remove((new_distance, v))
                new_distance = distances[current[1]][current[0]] + cavern_map[v[1]][v[0]]
                heapq.heappush(heap, (new_distance, v))
    print(distances[len(cavern_map) - 1][len(cavern_map[len(cavern_map) - 1]) - 1])


if __name__ == "__main__":
    main()
