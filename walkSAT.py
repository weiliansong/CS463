import numpy as np
import numpy.random as rand
from multiprocessing import Pool
from util import random_book, bool_eval

MAX_ITER = 1000000
MAX_REFRESH = 100000
REFRESH_ITER = 10000

def bool_swap(book, idx):
  temp = book[idx]
  book[idx] = book[-idx]
  book[-idx] = temp

  return book

def fitness_eval(tokens):
  book, var, clauses = tokens
  new_book = book.copy()
  new_book = bool_swap(new_book, var)

  return np.sum(bool_eval(clauses, new_book))

def solve(n_vars, clauses):
  clauses = np.array(clauses)
  book = random_book(n_vars)
  
  solved = False

  num_iter = 0
  num_refresh = 0

  while not solved and MAX_ITER-num_iter and MAX_REFRESH-num_refresh:
    clause_eval = bool_eval(clauses, book)
    fitness = np.sum(clause_eval)

    print('%d / %d' % (fitness, len(clauses)))

    if fitness == len(clauses):
      solved = True

    else:
      # Find index of clauses
      not_sat_idx = [i for i, fit in enumerate(clause_eval) if not fit]
      sat_idx = np.setdiff1d(np.arange(len(clauses)), not_sat_idx)

      # Find clauses
      sat_clauses = clauses[sat_idx]
      not_sat_clause = clauses[rand.choice(not_sat_idx)]

      # 80% chance for us to pick the best variable, 20% chance for random
      coin_toss = rand.choice([0,1], p=[0.1, 0.9])

      # We pick the best variable
      if coin_toss:
        best_fitness = 0
        best_var = None

        for var in not_sat_clause:
          fitness = fitness_eval((book, var, sat_clauses))

          if fitness > best_fitness:
            best_fitness = fitness
            best_var = var

        book = bool_swap(book, best_var)

      # We pick a random variable
      else:
        book = bool_swap(book, rand.choice(not_sat_clause))

      num_iter += 1

      if not (num_iter % REFRESH_ITER):
        print('Stuck at local min, randomizing assignments')
        book = random_book(n_vars)
        num_refresh += 1

  return solved
