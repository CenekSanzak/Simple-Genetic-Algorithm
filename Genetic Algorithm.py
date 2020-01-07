from queue import PriorityQueue
import random

target = "ceneksanzak"
target_length = len(target)
alphabet = "qwertyuıopğüasdfghjklşizxcvbnmöç "
population_size = 100
steps = 1000
periods = 10
kill_rate = 0.2
change_length = 3
mutation_rate = 0.01
population = []


def create_random_text(length):
    res = ""
    for _ in range(length):
        res += alphabet[random.randint(0, len(alphabet)-1)]
    return res


def score(gene):
    sc = 0
    for i in range(target_length):
        if gene[i] == target[i]:
            sc += 1
    return sc


def mix_genes(gene1, gene2):
    new_gene = ""
    new_gene += gene1[0: target_length - change_length]
    new_gene += gene2[target_length - change_length: target_length]
    for i in range(target_length-1):
        if random.random() < mutation_rate:
            new_gene = new_gene[:i] + alphabet[random.randint(0, len(alphabet)-1)] + new_gene[i+1:]
    if random.random() < mutation_rate:
        new_gene = new_gene[:target_length-1] + alphabet[random.randint(0, len(alphabet)-1)]
    return new_gene


def create_population():
    for _ in range(population_size):
        population.append(create_random_text(target_length))


def next_generation():
    q = PriorityQueue()
    global population
    for gene in population:
        q.put((score(gene), gene))
    population = []
    for i in range(population_size):
        gene = q.get()
        if i > population_size*kill_rate:
            s, gene = gene
            population.append(gene)
    while len(population) < population_size:
        population.append(mix_genes(population[random.randint(0, len(population)-1)], population[random.randint(0, len(population)-1)]))


create_population()
for i in range(1000):
    if i%int(steps/periods) == 0:
        print(int(i/periods))
    next_generation()
print("Results:")
for i in range(len(population)):
    print(population[i])
