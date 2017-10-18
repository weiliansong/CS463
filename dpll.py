import numpy as np
import numpy.random as rand
from multiprocessing import Pool
from util import random_book, bool_eval

def solve(n_vars, clauses):
  book = random_book()
  return dpll(n_vars, np.copy(clauses), book.copy())

def dpll(n_vars, clauses, book):

  clause_eval = bool_eval(clauses, book)
  fitness = np.sum(clause_eval)

  if fitness == len(clauses):
    return True

  vars_to_delete = []
  clauses_to_delete = []

  first, second = np.unique(np.concatenate(clauses), return_count=True)
  var_counts = dict(zip(first, second))

  for var in range(1, n_vars+1):
    if len(var_counts[var]) == 1 and len(var_counts[-var]) == 0:
      book[var] = 1
      book[-var] = 0
      vars_to_delete.append(var)

    elif len(var_counts[var]) == 0 and len(var_counts[-var]) == 1:
      book[var] = 0
      book[-var] = 1
      vars_to_delete.append(-var)

  for idx, clause in enumerate(clauses):
    if len(clause) == 0:
      return False
    
    elif len(clause) == 1:
      var = clause[0]
      book[var] = 1
      book[-var] = 0
      clauses_to_delete.append(idx)

    for var in vars_to_delete:
      if var in clause:
        clauses_to_delete.append(idx)

  # Delete all the single-variable clause
  clauses = np.delete(clauses, things_to_delete) 
