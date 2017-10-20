import numpy as np
import numpy.random as rand
from util import random_book, bool_eval, get_args

args = get_args()

MAX_ITER = 100
MAX_FLIP = 1000

# Flips assignment of a variable
def bool_swap(book, idx):
  temp = book[idx]
  book[idx] = book[-idx]
  book[-idx] = temp

  return book

# Flips assignment of a variable, then evaluate its performance by how many
# clauses it satisfied
def fitness_eval(tokens):
  book, var, clauses = tokens
  new_book = book.copy()
  new_book = bool_swap(new_book, var)

  return np.sum(bool_eval(clauses, new_book))

def solve(n_vars, clauses):
  max_fitness = 0

  for i in range(MAX_ITER):
    # Get a random assignment
    book = random_book(n_vars)

    # If we reaches maximum flips, we restart
    for j in range(MAX_FLIP):
      clause_eval = bool_eval(clauses, book)
      fitness = np.sum(clause_eval)

      if args.debug:
        print('%d / %d' % (fitness, len(clauses)))

      # If we solved all the clauses
      if fitness == len(clauses):
        return True, fitness
      else:
        if fitness > max_fitness:
          max_fitness = fitness

      # Find index of not satisfied clauses
      not_sat_idx = [i for i, fit in enumerate(clause_eval) if not fit]
      not_sat_clause = clauses[rand.choice(not_sat_idx)]

      # 50% chance for us to pick the best variable, 50% chance for random
      coin_toss = rand.choice([0,1])

      # We pick the best variable
      if coin_toss:
        best_fitness = 0
        best_var = None

        for var in not_sat_clause:
          fitness = fitness_eval((book, var, clauses))

          # See if flipping this var does any better
          if fitness > best_fitness:
            best_fitness = fitness
            best_var = var

        book = bool_swap(book, best_var)

      # We pick a random unsatisfied variable
      else:
        book = bool_swap(book, rand.choice(not_sat_clause))

  return False, max_fitness
