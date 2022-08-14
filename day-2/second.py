class Command:
    def __init__(self, function, parameter):
        self.function = function
        self.parameter = parameter


def main():
    depth = 0
    position = 0
    aim = 0

    f = open('./input.txt', 'r')
    commands = []
    for line in f:
        line = line.strip().split(' ')
        commands.append(Command(line[0], int(line[1])))

    for command in commands:
        if command.function == 'forward':
            position += command.parameter
            depth += aim * command.parameter
        elif command.function == 'down':
            aim += command.parameter
        elif command.function == 'up':
            aim -= command.parameter

    print(depth * position)


if __name__ == '__main__':
    main()
