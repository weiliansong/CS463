import numpy as np
import numpy.random as rand
from multiprocessing import Pool
from util import bool_eval

def solve(n_vars, clauses):

  if not len(clauses):
    return True

  vars_to_delete = []
  clauses_to_delete = []

  variables, counts = np.unique(np.concatenate(clauses), return_counts=True)
  var_counts = dict(zip(variables, counts))

  for var in range(1, n_vars+1):
    if var not in var_counts.keys():
      var_counts[var] = 0

    if -var not in var_counts.keys():
      var_counts[-var] = 0

  for var in range(1, n_vars+1):
    if var not in var_counts.keys():
      continue

    if var_counts[var] and var_counts[-var] == 0:
      vars_to_delete.append(var)

    elif var_counts[var] == 0 and var_counts[-var]:
      vars_to_delete.append(-var)

    else:
      continue

  for idx, clause in enumerate(clauses):
    if len(clause) == 0:
      return False
    
    # Check for unit clause
    elif len(clause) == 1:
      var = clause[0]
      if var_counts[var] and not var_counts[-var]:
        clauses_to_delete.append(idx)
        continue

    for var in vars_to_delete:
      if var in clause:
        clauses_to_delete.append(idx)

  # Delete all the single-variable clause
  clauses = np.delete(clauses, clauses_to_delete, axis=0) 

  # Finished with pruning, picking one random variable to set true
  lucky_var = rand.choice(np.unique(np.concatenate(clauses)))

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

  return solve(n_vars, true_clauses) or solve(n_vars, false_clauses)
