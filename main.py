import os
import time
import walkSAT, genetic, dpll, dpll_new
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

# WalkSAT solving
ensure_dir('./stats_WalkSAT')
fname = util.get_csv_name(args.input_file, 'stats_WalkSAT')

with open(fname, 'w') as f:
  f.write('fitness,time\n')

  for i in range(1):
    if args.verbose:
      print('[*] Solving %s with WalkSAT...' % args.input_file)

    solved, fitness, runtime = time_it(n_vars, clauses, walkSAT)

    if args.verbose:
      print('[Y] Max Fit: %3d/%3d | Time: %4.4f seconds | Solved: %s' 
              % (fitness, len(clauses), runtime, solved))

    f.write('%d,%.4f\n' % (fitness, runtime))

# Genetic solving
ensure_dir('./stats_Genetic')
fname = util.get_csv_name(args.input_file, 'stats_Genetic')

with open(fname, 'w') as f:
  f.write('fitness,time\n')

  for i in range(1):
    if args.verbose:
      print('[*] Solving %s with Genetic...' % args.input_file)

    solved, fitness, runtime = time_it(n_vars, clauses, genetic)

    if args.verbose:
      print('[Y] Max Fit: %3d/%3d | Time: %4.4f seconds | Solved: %s' 
              % (fitness, len(clauses), runtime, solved))

    f.write('%d,%.4f\n' % (fitness, runtime))

# DPLL solving
ensure_dir('./stats_DPLL')
fname = util.get_csv_name(args.input_file, 'stats_DPLL')

with open(fname, 'w') as f:
  f.write('fitness,time\n')

  for i in range(1):
    if args.verbose:
      print('[*] Solving %s with DPLL...' % args.input_file)

    solved, fitness, runtime = time_it(n_vars, clauses, dpll_new)

    if args.verbose:
      print('[Y] Max Fit: %3d/%3d | Time: %4.4f seconds | Solved: %s' 
              % (fitness, len(clauses), runtime, solved))

    f.write('%d,%.4f\n' % (fitness, runtime))
