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


def score(gen):
    sc = 0
    for i in range(target_length):
        if gen[i] == target[i]:
            sc += 1
    return sc


def mix_gens(gen1, gen2):
    new_gen = ""
    new_gen += gen1[0: target_length - change_length]
    new_gen += gen2[target_length - change_length: target_length]
    for i in range(target_length-1):
        if random.random() < mutation_rate:
            new_gen = new_gen[:i] + alphabet[random.randint(0, len(alphabet)-1)] + new_gen[i+1:]
    if random.random() < mutation_rate:
        new_gen = new_gen[:target_length-1] + alphabet[random.randint(0, len(alphabet)-1)]
    return new_gen


def create_population():
    for _ in range(population_size):
        population.append(create_random_text(target_length))


def next_generation():
    q = PriorityQueue()
    global population
    for gen in population:
        q.put((score(gen), gen))
    population = []
    for i in range(population_size):
        gen = q.get()
        if i > population_size*kill_rate:
            s, gen = gen
            population.append(gen)
    while len(population) < population_size:
        population.append(mix_gens(population[random.randint(0, len(population)-1)], population[random.randint(0, len(population)-1)]))


create_population()
for i in range(1000):
    if i%int(steps/periods) == 0:
        print(int(i/periods))
    next_generation()
print("Results:")
for i in range(len(population)):
    print(population[i])
