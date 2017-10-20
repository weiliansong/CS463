import numpy as np

# For each variable, this tells us how many times it has appeared in clauses
def get_var_counts(clauses):
  var_counts = {}

  for clause in clauses:
    for var in clause:
      # Initialize an empty if a variable isn't in it already
      if var not in var_counts.keys():
        var_counts[var] = 0

      var_counts[var] += 1

  return var_counts

# Checks to see if a variable is pure
def is_pure(var, var_counts):
  if -var not in var_counts.keys():
    # If the negation of var does not appear, then it's true
    return True
  elif var_counts[var] and not var_counts[-var]:
    # Same concept, just another way to check
    return True
  else:
    return False

# Remove a var from clause
def remove_var(not_var, clause):
  new_clause = []

  for var in clause:
    # We add the variable as long as it's not the one we want to remove
    if var != not_var:
      new_clause.append(var)
  
  return new_clause

# Removes all clauses that contains the pure literal
def handle_pure(var, clauses):
  new_clauses = []

  for clause in clauses:
    if var not in clause:
      new_clauses.append(list(clause))

  return new_clauses

# If a clause has length 1 and contains our target variable, returen True
def is_unit(var, clauses):
  for clause in clauses:
    if len(clause) == 1 and clause[0] == var:
      return True

  return False

# Remove all clauses that contaisn our unit clause variable
# Also removes all instances of the negation of the var
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

# Returns new clauses, if we imagine all instances of var in clauses set to true
def set_true(var, clauses):
  new_clauses = []
  for clause in clauses:
    # If the negation of the var appears, remove just the -var
    if var not in clause and -var in clause:
      new_clauses.append(remove_var(-var, clause))

    # If the clause has nothing to do with var or -var
    elif var not in clause and -var not in clause:
      new_clauses.append(list(clause))

    else:
      continue
  
  return new_clauses

def solve(n_vars, clauses):
  if recursion(clauses):
    return True, len(clauses)
  else:
    return False, 0

def recursion(clauses):
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

  # Only recurse if we found pure literals
  if has_pure: 
    if recursion(clauses):
      return True


  has_unit = False
  # Handle unit clauses
  var_counts = get_var_counts(clauses)
  for var in var_counts.keys():
    if is_unit(var, clauses):
      has_unit = True
      clauses = handle_unit(var, clauses)

  # Only recurse if we found pure unit clauses 
  if has_unit:
    if recursion(clauses):
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

  if recursion(true_clauses) or recursion(false_clauses):
    return True
  else:
    return False
