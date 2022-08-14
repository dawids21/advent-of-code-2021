from enum import Enum


class Bracket(Enum):
    ROUND = 3
    SQUARE = 57
    BRACE = 1197
    ANGLE = 25137


def check_line(line):
    brackets = []
    for bracket in line:
        if bracket in ["(", "[", "{", "<"]:
            brackets.append(bracket)
        elif bracket == ")":
            last_bracket = brackets.pop()
            if last_bracket != "(":
                return Bracket.ROUND
        elif bracket == "]":
            last_bracket = brackets.pop()
            if last_bracket != "[":
                return Bracket.SQUARE
        elif bracket == "}":
            last_bracket = brackets.pop()
            if last_bracket != "{":
                return Bracket.BRACE
        elif bracket == ">":
            last_bracket = brackets.pop()
            if last_bracket != "<":
                return Bracket.ANGLE
    return None


def main():
    f = open("input.txt", "r")
    score = 0
    for line in f:
        illegal_bracket = check_line(line)
        score += illegal_bracket.value if illegal_bracket is not None else 0

    print(score)


if __name__ == '__main__':
    main()
