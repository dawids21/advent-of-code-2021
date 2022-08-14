from enum import Enum


class FoldDirection(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


def fold_horizontal(paper, y):
    new_paper = [[dot for dot in row] for row in paper[:y]]
    for i in range(len(paper[y + 1:])):
        new_paper[-i - 1] = [any(x) for x in zip(paper[y - i - 1], paper[y + i + 1])]
    return new_paper


def fold_vertical(paper, x):
    new_paper = []
    for row in paper:
        new_row = row[:x]
        for i in range(len(row[x + 1:])):
            new_row[-i - 1] = any([row[x - i - 1], row[x + i + 1]])
        new_paper.append(new_row)
    return new_paper


def main():
    file = open("input.txt", "r")
    folds = []
    dots = []
    for line in file:
        if line.strip() == "":
            continue
        elif line.startswith("fold"):
            split_line = line.strip().split("=")
            fold_direction = FoldDirection.HORIZONTAL if split_line[0][-1] == "y" else FoldDirection.VERTICAL
            folds.append((fold_direction, int(split_line[1])))
        else:
            split_line = line.strip().split(",")
            dots.append((int(split_line[0]), int(split_line[1])))
    num_of_rows = find_num_of_rows(dots)
    num_of_columns = find_num_of_columns(dots)
    paper = [[(x, y) in dots for x in range(num_of_columns)] for y in range(num_of_rows)]
    for fold in folds:
        if fold[0] == FoldDirection.HORIZONTAL:
            paper = fold_horizontal(paper, fold[1])
        else:
            paper = fold_vertical(paper, fold[1])
    for row in paper:
        for dot in row:
            print("#" if dot else "_", end="")
        print()


def count_dots(paper):
    return sum([row.count(True) for row in paper])


def find_num_of_columns(holes):
    num_of_columns = max(holes, key=lambda x: x[0])[0] + 1
    return num_of_columns


def find_num_of_rows(holes):
    num_of_rows = max(holes, key=lambda x: x[1])[1] + 1
    return num_of_rows


if __name__ == '__main__':
    main()
