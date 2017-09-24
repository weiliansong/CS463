import copy
import time
import numpy as np
from heapq import heappush, heappop

class Solver:

  def __init__(self):
    # All possible moves according to my rules
    self.possible_moves = [[0, 'cw'], [0, 'ccw'],
                           [1, 'cw'], [1, 'ccw'],
                           [4, 'cw'], [4, 'ccw']]

  # Make each move from puzzle and return each moved puzzle
  def neighbors(self, puzzle):
    puzzles = []

    for move in self.possible_moves:
      puzzle_cpy = copy.deepcopy(puzzle)
      puzzle_cpy.move(move[0], move[1])
      puzzles.append(puzzle_cpy)

    return zip(puzzles, self.possible_moves)

  # Implemented with inspiration from
  # http://www.redblobgames.com/pathfinding/a-star/implementation.html
  def a_star(self, start):
    frontier = []
    heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    final_state = None

    came_from[start] = None
    cost_so_far[start] = 0

    def contains(state):
      for key in cost_so_far.keys():
        if key.equal(state):
          return True

      return False
    
    def costs_less(state, cost):
      if state not in cost_so_far: return False

      return True if state < cost_so_far[state] else False

    while len(frontier):
      # for item in frontier:
      #   print(item)
      # print()
      # time.sleep(1)

      (c_priority, c_state) = heappop(frontier)

      if c_state.is_solved():
        final_state = c_state
        break

      for (p_state, p_move) in self.neighbors(c_state):
        new_cost = cost_so_far[c_state] + 28

        if not contains(p_state) or costs_less(p_state, new_cost):
          cost_so_far[p_state] = new_cost
          came_from[p_state] = c_state
          priority = new_cost + p_state.dist_heuristic()

          heappush(frontier, (new_cost, p_state))

    return final_state, came_from, cost_so_far
