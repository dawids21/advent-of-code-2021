# segments
# 00000
# 1   2
# 1   2
# 33333
# 4   5
# 4   5
# 66666


def decode_one(encoded_digits, decoded_digits, segments):
    chars = list(filter(lambda x: len(x) == 2, encoded_digits))[0]
    decoded_digits[1] = set([c for c in chars])


def decode_seven(encoded_digits, decoded_digits, segments):
    chars = list(filter(lambda x: len(x) == 3, encoded_digits))[0]
    decoded_digits[7] = set([c for c in chars])
    segments[0] = (decoded_digits[7] - decoded_digits[1]).pop()


def decode_four(encoded_digits, decoded_digits, segments):
    chars = list(filter(lambda x: len(x) == 4, encoded_digits))[0]
    decoded_digits[4] = set([c for c in chars])


def decode_eight(encoded_digits, decoded_digits, segments):
    chars = list(filter(lambda x: len(x) == 7, encoded_digits))[0]
    decoded_digits[8] = set([c for c in chars])


def decode_nine(encoded_digits, decoded_digits, segments):
    chars = list(filter(lambda x: len(x) == 6 and decoded_digits[4].issubset(x), encoded_digits))[0]
    decoded_digits[9] = set([c for c in chars])
    segments[6] = (decoded_digits[9] - decoded_digits[4] - set(segments[0])).pop()
    segments[4] = (decoded_digits[8] - decoded_digits[9]).pop()


def decode_six(encoded_digits, decoded_digits, segments):
    chars = list(filter(
        lambda x: len(x) == 6 and not decoded_digits[1].issubset(x) and set([char for char in x]) != decoded_digits[9],
        encoded_digits))[0]
    decoded_digits[6] = set([c for c in chars])
    segments[2] = (decoded_digits[1] - decoded_digits[6]).pop()


def decode_zero(encoded_digits, decoded_digits, segments):
    chars = list(filter(
        lambda x: len(x) == 6 and set([char for char in x]) != decoded_digits[9] and set([c for c in x]) !=
                  decoded_digits[6],
        encoded_digits))[0]
    decoded_digits[0] = set([c for c in chars])
    segments[3] = (decoded_digits[8] - decoded_digits[0]).pop()


def decode_two(encoded_digits, decoded_digits, segments):
    decoded_digits[2] = set([segments[x] for x in [0, 2, 3, 4, 6]])


def decode_three(encoded_digits, decoded_digits, segments):
    decoded_digits[3] = set([segments[x] for x in [0, 3, 6]]).union(decoded_digits[1])


def decode_five(encoded_digits, decoded_digits, segments):
    chars = list(filter(
        lambda x: len(x) == 5 and set([char for char in x]) != decoded_digits[2] and set([c for c in x]) !=
                  decoded_digits[3],
        encoded_digits))[0]
    decoded_digits[5] = set([c for c in chars])


def main():
    f = open('input.txt', 'r')
    inputs = [x.split(' | ') for x in f]
    result = 0
    for i in inputs:
        encoded_digits = i[0].strip().split(" ")
        output = i[1].strip().split(" ")
        decoded_digits = [set() for _ in range(10)]
        segments = ["" for _ in range(7)]
        decode_one(encoded_digits, decoded_digits, segments)
        decode_seven(encoded_digits, decoded_digits, segments)
        decode_four(encoded_digits, decoded_digits, segments)
        decode_eight(encoded_digits, decoded_digits, segments)
        decode_nine(encoded_digits, decoded_digits, segments)
        decode_six(encoded_digits, decoded_digits, segments)
        decode_zero(encoded_digits, decoded_digits, segments)
        decode_two(encoded_digits, decoded_digits, segments)
        decode_three(encoded_digits, decoded_digits, segments)
        decode_five(encoded_digits, decoded_digits, segments)
        decoded_output = []
        for j in range(4):
            decoded_output.append([k for k in range(10) if set([c for c in output[j]]) == decoded_digits[k]][0])
        result += decoded_output[0] * 1000 + decoded_output[1] * 100 + decoded_output[2] * 10 + decoded_output[3]
    print(result)


if __name__ == '__main__':
    main()
