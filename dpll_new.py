import numpy as np

def get_var_counts(clauses):
  var_counts = {}

  for clause in clauses:
    for var in clause:
      if var not in var_counts.keys():
        var_counts[var] = 0

      var_counts[var] += 1

  return var_counts

def is_pure(var, var_counts):
  if -var not in var_counts.keys():
    return True
  elif var_counts[var] and not var_counts[-var]:
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
    if var not in clause:
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

    elif not_var in clause:
      new_clause = remove_var(not_var, clause)
      new_clauses.append(new_clause)

    else:
      new_clauses.append(clause)

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
  # print('begin')
  # print(clauses)
  # If we don't have any clauses
  if not len(clauses):
    return True

  # If we have an empty clause
  for clause in clauses:
    if len(clause) == 0:
      return False

  # Check
  var_counts = get_var_counts(clauses)

  has_pure = False
  # Handle pure literals
  for var in var_counts.keys():
    if is_pure(var, var_counts):
      has_pure = True
      clauses = handle_pure(var, clauses)
      # print('after each pure', var)
      # print(clauses)

  # print('after pure')
  # print(clauses)
  if has_pure: 
    if solve(clauses):
      # print('found pure')
      return True


  has_unit = False
  # Handle unit clauses
  var_counts = get_var_counts(clauses)
  for var in var_counts.keys():
    if is_unit(var, clauses):
      has_unit = True
      clauses = handle_unit(var, clauses)
      # print('after each unit', var)
      # print(clauses)

  # print('after unit')
  # print(clauses)
  if has_unit:
    if solve(clauses):
      # print('found unit')
      return True

  # Check again
  if not len(clauses):
    return True

  # If we have an empty clause
  for clause in clauses:
    if len(clause) == 0:
      return False
  
  var_counts = get_var_counts(clauses)
  # Picks a literal to flip
  lucky_var = np.random.choice(var_counts.keys())

  true_clauses = set_true(lucky_var, clauses)
  false_clauses = set_true(-lucky_var, clauses)

  if solve(true_clauses) or solve(false_clauses):
    return True
  else:
    return False
