# README #

## WalkSAT ##
Below is pseudocode for my WalkSAT program:

`
for i = 1 -> MAX ITER
  Generate random variable assignments

  for j = 1 -> MAX FLIP
    if we solved all clauses
      return True
    else
      if current fitness > max fitness
        max fitness = current fitness
    
    find all unsatisfied clauses

    flip a coin
    
    if coin == head
      find the best variable to flip that maximizes fitness
      flip the assignment of the variable

    if coin == tail
      choose random variable
      flip the assignment of the random variable

  return False
`    
