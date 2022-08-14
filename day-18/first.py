import json

from tree import Node


def main():
    file = open("input.txt", "r")
    numbers = [Node(json.loads(line), None) for line in file]
    ans = numbers[0]
    for i in numbers[1:]:
        ans = ans + i
    print(ans.magnitude())


if __name__ == '__main__':
    main()
