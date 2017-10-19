# https://github.com/domoritz/SoSAT/blob/master/sosat/genetic/algorithm.py
import numpy as np
import numpy.random as rand
from util import random_book, bool_eval, get_args

args = get_args()

def trace():
  import ipdb; ipdb.set_trace()

def print_chromo(chromo):
  for i in range(1, max(chromo)+1):
    print('%d: %d' % (i, chromo[i]))

max_population_size = 200
max_gen = 500
max_iters = 50
survival_rate = 0.10

crossover_rate = 0.5

mutation_rate = 0.5
mutation_percent = 0.05

def coin_toss(prob):
  return rand.choice([0,1], p=(1-prob,prob))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def fitness_eval(book, clauses):
  return np.sum(bool_eval(clauses, book))

def crossover(first, second, n_vars):
  offspring = first.copy()

  # Implementing single point crossover
  pivot_1 = rand.choice(range(1, n_vars+1))
  pivot_2 = rand.choice(range(pivot_1, n_vars+1))

  for i in range(pivot_1, pivot_2):
    offspring[i] = second[i]
    offspring[-i] = second[-i]

  return offspring

def mutate(book, n_vars):
  mutated_book = book.copy()
  num_mutations = int(mutation_percent * n_vars)
  mutate_vars = rand.choice(np.arange(1, n_vars+1), size=num_mutations)
  
  for var in mutate_vars:
    mutated_book[var] = book[-var]
    mutated_book[-var] = book[var]

  return mutated_book

# Check to see if this does what we want
def breed(first, second, n_vars):
  offspring = first.copy()
  
  if coin_toss(crossover_rate):
    offspring = crossover(first, second, n_vars)

  if coin_toss(mutation_rate):
    offspring = mutate(offspring, n_vars)

  return offspring 

def random_population(n):
  population = []
  for i in range(max_population_size):
    population.append(random_book(n))

  return np.array(population)

def solve(n_vars, clauses):

  best_fitness = 0

  for out_iter in range(max_iters):
    if args.debug:
      print('Restarting population')

    population = np.array(random_population(n_vars))

    last_best = 0
    last_gen = 0

    for gen_iter in range(max_gen):
      # Get the fitness of each member of the population
      fitnesses = []
      for individual in population:
        fitnesses.append(fitness_eval(individual, clauses))

      # Solved if # of solved clause in fitnesses
      if len(clauses) in fitnesses:
        return True, len(clauses)
      else:
        max_fitness = max(fitnesses)
        if args.debug:
          print('%d / %d : %d / %d' 
                  % (gen_iter, last_gen, max_fitness, len(clauses)))

        if max_fitness > last_best:
          last_gen = 0
          last_best = max_fitness

        elif last_best == max_fitness:
          last_gen += 1

        if last_gen >= 100:
          break

        if max_fitness > best_fitness:
          best_fitness = max_fitness

      # Sort population by their fitnesses
      population = population[np.argsort(fitnesses)[::-1]]
      fitnesses = np.sort(fitnesses)[::-1]

      # Kill off a portion of the population
      population = population[:int(survival_rate * max_population_size)]
      fitnesses = fitnesses[:int(survival_rate * max_population_size)]

      # Probability for each book in population to be picked, 90% to 10%
      prob = softmax(fitnesses)

      new_population = []
      for i in range(max_population_size - len(population)):
        first, second = rand.choice(population, size=2, p=prob)
        new_population.append(breed(first, second, n_vars))

      population = np.concatenate([population, new_population])

  return False, best_fitness
