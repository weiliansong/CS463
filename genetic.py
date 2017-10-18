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
  return rand.choice([0,1], p=(1-prob,prob))

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def fitness_eval(tokens):
  book, clauses = tokens

  return np.sum(bool_eval(clauses, book))

def crossover(first, second, n_vars):
  offspring = first.copy()

  if coin_toss(crossover_rate):
    # Implementing single point crossover
    pivot = int(rand.rand() * n_vars)

    for i in range(pivot, n_vars):
      offspring[i] = second[i]
      offspring[-i] = second[-i]

  return offspring

def mutate(book, n_vars):
  mutated_book = book.copy()
  num_mutations = np.round(mutation_percent * n_vars)
  mutate_vars = rand.choice(np.arange(1, n_vars+1), size=num_mutations)
  
  for var in mutate_vars:
    mutated_book[var] = book[-var]
    mutated_book[-var] = book[var]

  return mutated_book

# Check to see if this does what we want
def breed(tokens):
  first, second, n_vars = tokens
  offspring = crossover(first, second, n_vars)
  offspring = mutate(offspring, n_vars)

  return offspring 

def random_population(n):
  population = []
  for i in range(max_population_size):
    population.append(random_book(n))
  population = np.array(population)

  return population

def solve(n_vars, clauses):

  # Making population
  population = random_population(n_vars)

  total_gen = 0
  current_gen = 0
  max_fitness = 0
  last_gen = 0

  p = Pool(2)

  while True:

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
      first, second = rand.choice(population, size=2, p=prob)
      jobs.append((first, second, n_vars))

    np.concatenate(population, p.map(breed, jobs))

    current_gen += 1

    if (current_gen - last_gen) > gen_limit:
      total_gen += current_gen
      
      if total_gen > max_gen:
        return False

      else:
        current_gen = 0
        last_gen = 0
        max_fitness = 0
        population = random_population(n_vars)
