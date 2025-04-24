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
    return chromosome
