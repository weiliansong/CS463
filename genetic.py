# https://github.com/domoritz/SoSAT/blob/master/sosat/genetic/algorithm.py
import numpy as np
import numpy.random as rand
from util import random_book, bool_eval, get_args
from multiprocessing import Pool

args = get_args()

max_population_size = 200
max_gen = 500
max_iters = 2500
survival_rate = 0.20

crossover_rate = 0.2

mutation_rate = 0.4
mutation_percent = 0.05

def coin_toss(prob):
  return rand.choice([0,1], p=(1-prob,prob))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def fitness_eval(tokens):
  book, clauses = tokens

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
def breed(tokens):
  first, second, n_vars = tokens
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
  p = Pool(2)

  for out_iter in range(max_iters):
    if args.debug:
      print('Restarting population')

    population = np.array(random_population(n_vars))

    last_best = 0
    last_gen = 0

    for gen_iter in range(max_gen):

      # Get the fitness of each member of the population
      jobs = []
      for i in range(len(population)):
        jobs.append((population[i], clauses))
      
      fitnesses = p.map(fitness_eval, jobs)

      # Sanity check...
      assert len(fitnesses) == len(population)

      # Solved if # of solved clause in fitnesses
      if len(clauses) in fitnesses:
        return True, len(clauses)
      else:
        max_fitness = max(fitnesses)
        if args.debug:
          print('%d / %d : %d / %d' 
                  % (gen_iter, last_gen ,max_fitness,best_fitness))

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
      # TODO Check and make sure this works...
      population = population[np.argsort(fitnesses)[::-1]]
      fitnesses = np.sort(fitnesses)[::-1]

      # Kill off a portion of the population
      population = population[:int(survival_rate * max_population_size)]
      fitnesses = fitnesses[:int(survival_rate * max_population_size)]

      # Probability for each book in population to be picked, 90% to 10%
      prob = softmax(fitnesses)

      jobs = []
      for i in range(max_population_size - len(population)):
        first, second = rand.choice(population, size=2, p=prob)
        jobs.append((first, second, n_vars))

      population = np.concatenate([population, p.map(breed, jobs)])

  return False, best_fitness
