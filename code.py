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
  
