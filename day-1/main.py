def first():
    f = open('./input.txt', 'r')

    readings = [int(x.strip()) for x in f]

    num_of_increments = 0
    for i in range(1, len(readings)):
        if readings[i - 1] < readings[i]:
            num_of_increments += 1

    print(num_of_increments)


def second():
    f = open('./input.txt', 'r')

    readings = [int(x.strip()) for x in f]
    sliding_windows = [readings[i] + readings[i + 1] + readings[i + 2] for i in range(len(readings) - 2)]

    num_of_increments = 0
    for i in range(1, len(sliding_windows)):
        if sliding_windows[i - 1] < sliding_windows[i]:
            num_of_increments += 1

    print(num_of_increments)


if __name__ == '__main__':
    # first()
    second()
