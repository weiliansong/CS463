import time
import util
import WalkSAT 
import numpy as np
from multiprocessing import Pool

f = open('easy.cnf', 'r')
lines = f.readlines()
f.close()

clauses = []

for line in lines:
  line = line.strip()

  if line[0] in ['p', 'c']:
    continue
  
  if line[-1] != '0':
    raise Exception('Last char not 0')

  clause = [int(x) for x in line.split(' ')[:-1] if x]

  clauses.append(clause)

start = time.time()
solved = WalkSAT.solve(100, clauses)
end = time.time()

print(solved)
print(end - start)
