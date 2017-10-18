import numpy as np
import numpy.random as rand
from multiprocessing import Pool
from util import random_book, bool_eval

def solve(n_vars, clauses):
  book = random_book()
  return helper(n_vars, clauses, book)

def helper(n_vars, clauses, book):

  clause_eval = bool_eval(clauses, book)
  fitness = np.sum(clause_eval)

  if fitness == len(clauses):
    return True

  vars_to_delete = []
  clauses_to_delete = []

  variables, counts = np.unique(np.concatenate(clauses), return_count=True)
  var_counts = dict(zip(variables, counts))

  for var in range(1, n_vars+1):
    if len(var_counts[var]) and len(var_counts[-var]) == 0:
      book[var] = 1
      book[-var] = 0
      vars_to_delete.append(var)

    elif len(var_counts[var]) == 0 and len(var_counts[-var]):
      book[var] = 0
      book[-var] = 1
      vars_to_delete.append(-var)

    else:
      continue

  for idx, clause in enumerate(clauses):
    if len(clause) == 0:
      return False
    
    # Check for unit clause
    elif len(clause) == 1:
      var = clause[0]
      book[var] = 1
      book[-var] = 0
      clauses_to_delete.append(idx)
      continue

    for var in vars_to_delete:
      if var in clause:
        clauses_to_delete.append(idx)

  # Delete all the single-variable clause
  clauses = np.delete(clauses, things_to_delete) 

  # Finished with pruning, picking one random variable to set true
  lucky_var = np.choice(np.unique(np.concatenate(clauses)))

  true_clauses = []
  false_clauses = []

  for clause in clauses:
    if lucky_var in clause and -lucky_var not in clause:
      clause = np.delete(clause, np.where(clause==lucky_var))
      false_clauses.append(clause)

    elif lucky_var not in clause and -lucky_var in clause:
      clause = np.delete(clause, np.where(clause==-lucky_var))
      true_clauses.append(clause)

    elif lucky_var in clause and -lucky_var in clause:
      continue
    
    else:
      true_clauses.append(clause)
      false_clauses.append(clause)

  return helper(n_vars, true_clauses) or helper(n_vars, false_clauses)
