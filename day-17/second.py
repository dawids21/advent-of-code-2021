import math


def get_max_reached_x(x):
    return sum(range(1, x + 1))


def find_possible_steps(x, target_x):
    possible_steps = []
    for step in range(1, x + 2):
        end_x = sum(range(x - step + 1, x + 1))
        if target_x[0] <= end_x <= target_x[1]:
            possible_steps.append(step)
    return possible_steps


def main():
    target_x = (209, 238)
    target_y = (-86, -59)
    velocities = set()
    for x in range(1, target_x[1] + 1):
        if x > target_x[1]:
            continue
        possible_steps = find_possible_steps(x, target_x)
        if not possible_steps:
            continue
        reached_max_x = possible_steps[-1] == x + 1
        for step in possible_steps:
            sum_step = sum(range(step))
            for y in range(math.ceil((target_y[0] + sum_step) / step),
                           math.floor((target_y[1] + sum_step) / step) + 1):
                velocities.add((x, y))
        if possible_steps[-1] != x + 1:
            continue
        for y in range(-target_y[0] + 1):
            current_y = 0
            step = 1
            while current_y > target_y[1] and current_y >= target_y[0]:
                current_y += -y - step
                step += 1
            if 2 * y + 1 + step >= possible_steps[-1] and current_y >= target_y[0]:
                velocities.add((x, y))

    print(len(velocities))


if __name__ == '__main__':
    main()
