import time
import util
import walkSAT 
import genetic
import dpll
import numpy as np
import argparse
from multiprocessing import Pool

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='input_file', action='store', type=str)

args = parser.parse_args()

f = open(args.input_file, 'r')
lines = f.readlines()
f.close()

clauses = []
n_vars = -1

for line in lines:
  line = line.strip()

  if line[0] == 'c':
    continue
  elif line[0] == 'p':
    n_vars = int(line.split(' ')[2])
    continue
  
  if line[-1] != '0':
    raise Exception('Last char not 0')

  clause = [int(x) for x in line.split(' ')[:-1] if x]

  clauses.append(clause)

clauses = np.array(clauses)

print('Num vars: %d' % n_vars)

start = time.time()
solved = dpll.solve(n_vars, clauses)
end = time.time()

print(solved)
print(end - start)
