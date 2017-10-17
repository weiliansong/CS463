import numpy as np
import numpy.random as rand

def fitness_eval(tokens):
  book, var, clauses = tokens
  new_book = book.copy()
  new_book = bool_swap(new_book, var)

  return np.sum(bool_eval(clauses, new_book))

def Genetic(self):
  total_gen = 1
  current_gen = 1
  max_fitness = 0

  population = []
  for i in range(self.max_population_size):
    population.append(random_book(self.n_vars))


