import time
import numpy as np
import matplotlib.pyplot as plt

from solver import Solver
from puzzle import Puzzle
from visualizer import Visualizer
from randomizer import Randomizer

visualizer = Visualizer()

# =========================================================================== #
# Below is code for automating and plotting nodes expansion needed for each
# depth k solution. The code is commented out due to A* being very slow and
# Testing with any reasonable K would take ages...
#
# # Contains average number of nodes expanded for each case k
# nodes_expanded_list = []
# 
# k = int(input('K value to test up to: '))
# 
# for k_idx in range(1, k+1):
#   print('\n-----------Case k = %d-----------' % k_idx)
# 
#   # Contains number of nodes expanded for each of the 5 trials of 
#   # k-randomized puzzle
#   nodes_expanded_k = []
# 
#   for case_idx in range(5):
#     puzzle = Puzzle()
#     rand = Randomizer()
#     solver = Solver()
#     moves = []
# 
#     for _ in range(k_idx):
#       move = rand.get_random_move()
#       puzzle.move(move[0], move[1])
# 
#     start = time.time()
#     final, path, cost, nodes_expanded = solver.a_star(puzzle)
#     solved = solver.fix_edges(final)
#     end = time.time()
# 
#     print('Case %d' % (case_idx+1))
#     print('Time: %.4f seconds' % (end-start))
#     print('Num nodes expanded: %d\n' % nodes_expanded)
# 
#     nodes_expanded_k.append(nodes_expanded)
# 
#   nodes_expanded_avg = np.sum(nodes_expanded_k) / len(nodes_expanded_k)
#   nodes_expanded_list.append(nodes_expanded_avg)
# 
# # Plotting results
# plt.clf()
# plt.plot(range(1, len(nodes_expanded_list) + 1), nodes_expanded_list, '-o')
# plt.xticks(range(1, len(nodes_expanded_list) + 1))
# plt.xlabel('Supposed depth of tree')
# plt.ylabel('Nodes expanded')
# plt.title('Depth of tree vs. nodes expanded')
# plt.show()
# =========================================================================== #

# =========================================================================== #
# Below is runnable code that creates a puzzle, takes in user input k,
# randomizes with k moves, and tries to solve it. I have tried k <= 6 and they
# take an awful amount of time, like ~30 mins for k = 6.
puzzle = Puzzle()
rand = Randomizer()
solver = Solver()
moves = []

# Asks user for number of random moves
num_moves = int(input('How many random moves: '))

for idx in range(num_moves):
  moves.append(rand.get_random_move())

for move in moves:
  print(move)

for move in moves:
  puzzle.move(move[0], move[1])

start = time.time()
final_state, came_from, cost_so_far, nodes_expanded = solver.a_star(puzzle)
final_state = solver.fix_edges(final_state)
end = time.time()

print('\nTime: %.4f seconds' % (end-start))
print('Num nodes expanded: %d\n' % nodes_expanded)
visualizer.visualize(final_state)
