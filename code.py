import random
def random_chromosome(n):   
    return [random.randint(0, n-1) for _ in range(n)]

def fitness(chromosome):
     n = len(chromosome)
     conflicts = 0
     for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
     return -conflicts

def probability(population):
    fitness_values = [fitness(ch) for ch in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return probabilities     
  


def random_pick(population, probabilities):
    return random.choices(population, weights=probabilities, k=1)[0]



def cross_over(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n-2)
    return parent1[:point] + parent2[point:]



def mutate(chromosome, mutation_rate=0.1):
    n = len(chromosome)
    if random.random() < mutation_rate:   #با یک احتمال کوچک  مقداری در کروموزوم را تغییر می‌دهد.
        i = random.randint(0, n-1)
        chromosome[i] = random.randint(0, n-1)




def genetic_queen(n, population_size=100, generations=1000, mutation_rate=0.1):
    population = [random_chromosome(n) for _ in range(population_size)]
    for generation in range(generations):
        probabilities = probability(population)
        new_population = []
        for _ in range(population_size):
            parent1 = random_pick(population, probabilities)
            parent2 = random_pick(population, probabilities)
            child = cross_over(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population
         # بررسی کروموزوم بدون برخورد
        for chromosome in population:
            if fitness(chromosome) == 0:
                return chromosome, generation    return chromosome
 for chromosome in population:
            if fitness(chromosome) == 0:
                return chromosome, generation

    return None, generations
