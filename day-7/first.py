def main():
    f = open('input.txt', 'r')
    crabs = [int(crab) for crab in f.readline().strip().split(',')]
    min_crab = min(crabs)
    max_crab = max(crabs)
    min_fuel = -1
    for place in range(min_crab, max_crab + 1):
        current = sum(map(lambda x: abs(place - x), crabs))
        if min_fuel == -1:
            min_fuel = current
        else:
            min_fuel = min(min_fuel, current)
    print(min_fuel)


if __name__ == '__main__':
    main()
