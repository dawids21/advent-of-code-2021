def find_most_common_at(nums, index):
    num_of_digits = [0, 0]
    for num in nums:
        num_of_digits[int(num[index])] += 1
    return '1' if num_of_digits[1] >= num_of_digits[0] else '0'


def find_least_common_at(nums, index):
    num_of_digits = [0, 0]
    for num in nums:
        num_of_digits[int(num[index])] += 1
    return '0' if num_of_digits[0] <= num_of_digits[1] else '1'


def main():
    f = open('./input.txt', 'r')
    nums = [x.strip() for x in f]

    current = [x for x in nums]
    for i in range(len(nums[0])):
        most_common = find_most_common_at(current, i)
        current = list(filter(lambda x: x[i] == most_common, current))
        if len(current) == 1:
            break
    print(current)
    current = [x for x in nums]
    for i in range(len(nums[0])):
        least_common = find_least_common_at(current, i)
        current = list(filter(lambda x: x[i] == least_common, current))
        if len(current) == 1:
            break
    print(current)


if __name__ == '__main__':
    main()
