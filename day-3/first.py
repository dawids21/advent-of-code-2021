def main():
    f = open('./input.txt', 'r')
    nums = [x.strip() for x in f]

    gamma_rate = ''
    for i in range(len(nums[0])):
        num_of_digits = [0, 0]
        for n in nums:
            num_of_digits[int(n[i])] += 1
        gamma_rate += '0' if num_of_digits[0] > num_of_digits[1] else '1'

    print(gamma_rate)


if __name__ == '__main__':
    main()
