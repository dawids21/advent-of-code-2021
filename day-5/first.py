from enum import Enum, auto


class Direction(Enum):
    HORIZONTAL = auto()
    DIAGONAL_45 = auto()
    VERTICAL = auto()
    DIAGONAL_135 = auto()
    DIAGONAL_225 = auto()
    DIAGONAL_315 = auto()


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_points(self):
        direction = self.get_direction()
        if direction == Direction.VERTICAL:
            return [(self.start[0], y) for y in
                    range(min(self.start[1], self.end[1]), self.get_max_y() + 1)]
        elif direction == Direction.HORIZONTAL:
            return [(x, self.start[1]) for x in
                    range(min(self.start[0], self.end[0]), self.get_max_x() + 1)]
        elif direction == Direction.DIAGONAL_45:
            points = []
            for i in range(self.end[0] - self.start[0] + 1):
                points.append((self.start[0] + i, self.start[1] + i))
            return points
        elif direction == Direction.DIAGONAL_135:
            points = []
            for i in range(self.end[1] - self.start[1] + 1):
                points.append((self.start[0] - i, self.start[1] + i))
            return points
        elif direction == Direction.DIAGONAL_225:
            points = []
            for i in range(self.start[0] - self.end[0] + 1):
                points.append((self.start[0] - i, self.start[1] - i))
            return points
        elif direction == Direction.DIAGONAL_315:
            points = []
            for i in range(self.start[1] - self.end[1] + 1):
                points.append((self.start[0] + i, self.start[1] - i))
            return points
        return []

    def get_direction(self):
        if self.start[0] == self.end[0]:
            return Direction.VERTICAL
        elif self.start[1] == self.end[1]:
            return Direction.HORIZONTAL
        elif self.end[0] - self.start[0] == self.end[1] - self.start[1]:
            if self.end[0] > self.start[0]:
                return Direction.DIAGONAL_45
            return Direction.DIAGONAL_225
        elif self.start[0] - self.end[0] == self.end[1] - self.start[1]:
            if self.start[0] > self.end[0]:
                return Direction.DIAGONAL_135
            return Direction.DIAGONAL_315
        return None

    def get_min_x(self):
        return min(self.start[0], self.end[0])

    def get_min_y(self):
        return min(self.start[1], self.end[1])

    def get_max_x(self):
        return max(self.start[0], self.end[0])

    def get_max_y(self):
        return max(self.start[1], self.end[1])


class Diagram:
    def __init__(self, x, y):
        self.table = [[0 for _ in range(x)] for _ in range(y)]

    def mark(self, points):
        for point in points:
            self.table[point[1]][point[0]] += 1

    def get_dangerous_area(self):
        return [(x, y) for x in range(len(self.table[0])) for y in range(len(self.table)) if self.table[y][x] >= 2]


def main():
    file = open('./input.txt', 'r')

    lines = []
    for file_line in file:
        points = file_line.split('->')
        points = list(map(lambda x: tuple(map(lambda y: int(y), x.strip().split(','))), points))
        lines.append(Line(points[0], points[1]))

    diagram = Diagram(max([line.get_max_x() for line in lines]) + 1, max([line.get_max_y() for line in lines]) + 1)

    for line in lines:
        points = line.get_points()
        diagram.mark(points)

    dangerous_points = diagram.get_dangerous_area()

    print(len(dangerous_points))


if __name__ == '__main__':
    main()
