def main():
    f = open('input.txt', 'r')
    outputs = [x.split(' | ')[1].strip() for x in f]
    num_of_tracked_digits = 0
    for output in outputs:
        digits = output.split(" ")
        num_of_tracked_digits += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], digits)))
    print(num_of_tracked_digits)


if __name__ == '__main__':
    main()
