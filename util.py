import numpy as np
import numpy.random as random
from multiprocessing import Pool

def random_book(n_vars):
  book = {}

  for i in range(1, n_vars+1):
    book[i] = random.choice([0,1])
    book[-i] = (book[i] + 1) % 2
  
  return book

def bool_or(clause, book):
  for var in clause:
    if book[var]:
      return 1

  return 0

def bool_eval(clauses, book):
  results = []

  for clause in clauses:
    results.append(bool_or(clause, book))

  return results
