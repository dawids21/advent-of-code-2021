def check_line(line):
    brackets = []
    for bracket in line:
        if bracket in ["(", "[", "{", "<"]:
            brackets.append(bracket)
        elif bracket == ")":
            last_bracket = brackets.pop()
            if last_bracket != "(":
                return None
        elif bracket == "]":
            last_bracket = brackets.pop()
            if last_bracket != "[":
                return None
        elif bracket == "}":
            last_bracket = brackets.pop()
            if last_bracket != "{":
                return None
        elif bracket == ">":
            last_bracket = brackets.pop()
            if last_bracket != "<":
                return None
    return brackets


def main():
    f = open("input.txt", "r")
    scores = []
    map_of_scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    for line in f:
        brackets = check_line(line)
        if brackets is not None and len(brackets) > 0:
            current_score = 0
            for bracket in brackets[::-1]:
                current_score *= 5
                current_score += map_of_scores[bracket]
            scores.append(current_score)
    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == '__main__':
    main()
