import numpy as np
import numpy.random as rand
from util import random_book, bool_eval
from multiprocessing import Pool

max_population_size = 1000
max_generations = 10000
survival_rate = 0.75
gen_limit = 1000

crossover_rate = 0.5
mutation_rate = 0.5
mutation_percent = 0.1

def coin_toss(prob):
  return np.choice([0,1], p=(1-prob,prob))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def fitness_eval(tokens):
  book, clauses = tokens

  return np.sum(bool_eval(clauses, book))

# TODO Make sure this works...
def crossover(first, second, n_vars):
  offspring = first.copy()

  if coin_toss(crossover_rate):
    # Implementing single point crossover
    pivot = int(rand.rand() * n_vars)

    for i in range(pivot, len(first.keys())):
      offspring[i] = second[i]
      offspring[-i] = second[-i]

  return offspring

def mutate(book, n_vars):
  num_mutations = np.round(mutation_percent * len(book.keys()))
  mutate_vars = 

def breed(tokens):
  first, second, n_vars = tokens
  offspring = crossover(first, second, n_vars)
  offspring = mutate(offspring, n_vars)

  return offspring 

def solve(n_vars, clauses):

  # Making population
  population = []
  for i in range(max_population_size):
    population.append(random_book(n_vars))
  population = np.array(population)

  total_gen = 1
  current_gen = 1
  max_fitness = 0
  last_gen = 0

  p = Pool(2)

  while current_gen <= max_generations:

    # Get the fitness of each member of the population
    jobs = []
    for i in range(max_population_size):
      jobs.append((population[i], clauses))
    
    fitnesses = p.map(fitness_eval, jobs)

    # Sanity check...
    assert len(fitnesses) == len(population)

    # Solved if # of solved clause in fitnesses
    if len(clauses) in fitnesses:
      return True
    
    # Consider some speed up here?
    if max(fitnesses) > max_fitness:
      last_gen = current_gen
      max_fitness = max(fitnesses)

    # Sort population by their fitnesses
    # TODO Check and make sure this works...
    population = population[np.argsort(fitnesses)]

    # Kill off a portion of the population
    population = population[:int(survival_rate * max_population_size)]

    # Probability for each book in population to be picked, 90% to 10%
    prob = softmax(np.linspace(90, 10, num=len(population)))

    jobs = []
    for i in range(max_population_size - len(population)):
      first, second = np.choice(population, size=2, p=prob)
      jobs.append((first, second, n_vars))

    population.extend(p.map(breed, jobs))

    current_gen += 1

    if (current_gen - last_gen) > gen_limit:
      pass
