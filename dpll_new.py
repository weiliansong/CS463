import numpy as np

def clean_var_counts(var_counts):
  for i in range(1, 101):
    if i not in var_counts.keys():
      var_counts[i] = 0
    
    if -i not in var_counts.keys():
      var_counts[-i] = 0

  return var_counts

def get_var_counts(clauses):
  var_counts = {}

  for clause in clauses:
    for var in clause:
      if var not in var_counts.keys():
        var_counts[var] = 0

      var_counts[var] += 1

  return clean_var_counts(var_counts)

def is_pure(var, var_counts):
  if var_counts[var] and not var_counts[-var]:
    return True
  else:
    return False

def remove_var(not_var, clause):
  new_clause = []

  for var in clause:
    if var != not_var:
      new_clause.append(var)
  
  return new_clause

def handle_pure(var, clauses):
  new_clauses = []

  for clause in clauses:
    if var not in clauses:
      new_clauses.append(list(clause))

  return new_clauses

def is_unit(var, clauses):
  for clause in clauses:
    if len(clause) == 1 and clause[0] == var:
      return True

  return False

def handle_unit(unit_var, clauses):
  not_var = -unit_var

  new_clauses = []
  for clause in clauses:
    if unit_var in clause:
      continue

    if not_var in clause:
      new_clause = remove_var(not_var, clause)
      new_clauses.append(new_clause)

  return new_clauses

def set_true(var, clauses):
  new_clauses = []
  for clause in clauses:
    if var not in clause and -var in clause:
      new_clauses.append(remove_var(-var, clause))

    elif var not in clause and -var not in clause:
      new_clauses.append(list(clause))

    else:
      continue
  
  return new_clauses

def solve(clauses):
  # If we don't have any clauses
  if not len(clauses):
    return True, 1

  # If we have an empty clause
  for clause in clauses:
    if not len(clause):
      return False, 0

  var_counts = get_var_counts(clauses)

  has_pure = False
  # Handle pure literals
  for var in var_counts.keys():
    if is_pure(var, var_counts):
      has_pure = True
      clauses = handle_pure(var, clauses)

  if has_pure:
    return solve(clauses)

  has_unit = False
  # Handle unit clauses
  for var in var_counts.keys():
    if is_unit(var, clauses):
      has_unit = True
      clauses = handle_unit(var, clauses)

  if has_unit:
    return solve(clauses)
  
  # Picks a literal to flip
  lucky_var = np.random.choice(var_counts.keys())

  true_clauses = set_true(lucky_var, clauses)
  false_clauses = set_true(-lucky_var, clauses)

  if solve(true_clauses) or solve(false_clauses):
    return True, 1
  else:
    return False, 0
