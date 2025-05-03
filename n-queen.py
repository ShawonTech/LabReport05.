import random

def random_chromosome(size):
    return [random.randint(1, size) for _ in range(size)]

def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome]) / 2
    n = len(chromosome)
    left_diagonal = [0] * (2 * n)
    right_diagonal = [0] * (2 * n)

    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[n - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        if left_diagonal[i] > 1:
            diagonal_collisions += (left_diagonal[i] - 1)
        if right_diagonal[i] > 1:
            diagonal_collisions += (right_diagonal[i] - 1)

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

def probability(chromosome, fitness_func):
    return fitness_func(chromosome) / maxFitness

def random_pick(population, probabilities):
    r = random.uniform(0, sum(probabilities))
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    return population[0]

def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(population, fitness_func):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness_func) for n in population]

    for i in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)

        if random.random() < mutation_probability:
            child = mutate(child)

        print_chromosome(child)
        new_population.append(child)

        if fitness_func(child) == maxFitness:
            break

    return new_population

def print_chromosome(chrom):
    print("Chromosome = {}, Fitness = {}".format(str(chrom), fitness(chrom)))

def print_board(board):
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: "))
    maxFitness = (nq * (nq - 1)) / 2
    population = [random_chromosome(nq) for _ in range(100)]

    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1

    print("Solved in Generation {}!".format(generation - 1))

    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("\nOne of the solutions: ")
            print_chromosome(chrom)
            chrom_out = chrom
            Break

    board = [["x"] * nq for _ in range(nq)]
    for i in range(nq):
        board[nq - chrom_out[i]][i] = "Q"

    print()
    print_board(board)

