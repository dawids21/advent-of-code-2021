import json

from tree import Node


def main():
    file = open("input.txt", "r")
    numbers = [Node(json.loads(line), None) for line in file]
    ans = 0
    for i in numbers:
        for j in numbers:
            if i != j:
                ans = max(ans, (i + j).magnitude())
    print(ans)


if __name__ == '__main__':
    main()
