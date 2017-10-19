import os
import time
import walkSAT, genetic, dpll
import util
import numpy as np
from multiprocessing import Pool

args = util.get_args()

clauses, n_vars = util.get_clauses()

def time_it(n_vars, clauses, algorithm):
  start = time.time()
  solved, c = algorithm.solve(n_vars, clauses)
  end = time.time()

  return solved, c, end-start

def ensure_dir(directory):
  if not os.path.exists(directory):
    os.mkdir(directory)

# Lol...
if args.lol:
  print('[*] Solving %s...' % args.input_file)
  import pycosat
  print(pycosat.solve(clauses))
  exit()

ensure_dir('./stats')

# WalkSAT solving
fname = util.get_csv_name(args.input_file)

with open(fname, 'w') as f:
  f.write('fitness,time\n')

  for i in range(10):
    if args.verbose:
      print('[*] Solving %s...' % args.input_file)

    solved, fitness, runtime = time_it(n_vars, clauses, genetic)

    if args.verbose:
      print('[Y] Max Fit: %3d/%3d | Time: %4.4f seconds | Solved: %s' 
              % (fitness, len(clauses), runtime, solved))

    f.write('%d,%.4f\n' % (fitness, runtime))
