import time
import argparse
import numpy as np
import numpy.random as random

def random_book(n_vars):
  book = {}

  for i in range(1, n_vars+1):
    book[i] = random.choice([0,1])
    book[-i] = (book[i] + 1) % 2
  
  return book

def bool_or(clause, book):
  for var in clause:
    if book[var]:
      return 1

  return 0

def bool_eval(clauses, book):
  results = []

  for clause in clauses:
    results.append(bool_or(clause, book))

  return results

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', dest='input_file', action='store', type=str)
  parser.add_argument('--debug', dest='debug', action='store_true', 
                      default=False)
  parser.add_argument('--lol', dest='lol', action='store_true', 
                      default=False)
  parser.add_argument('--verbose', dest='verbose', action='store_true', 
                      default=False)

  args = parser.parse_args()

  return args

def get_clauses():
  args = get_args()

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

  return clauses, n_vars

def get_csv_name(input_file, method):
  cnf_fname = input_file.strip().split('/')[-1]
  cnf_fname = cnf_fname[:-4].replace('.', '_')
  return './' + method + '/' + cnf_fname + '.csv'
