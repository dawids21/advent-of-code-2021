def generate_next_population(population):
    zero = population[0]
    population = population[1:]
    population[6] += zero
    population.append(zero)
    return population


def main():
    f = open('./input.txt', 'r')

    population = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in f.readline().split(','):
        population[int(x)] += 1

    for i in range(256):
        population = generate_next_population(population)
    print(sum(population))


if __name__ == '__main__':
    main()
