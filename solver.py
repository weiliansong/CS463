import copy
import time
import numpy as np
from heapq import heappush, heappop

class Solver:

  def __init__(self):
    # All possible moves according to my rules
    # I only allow the left(0), front(1), and top(4) face to rotate
    self.possible_moves = [[0, 'cw'], [0, 'ccw'],
                           [1, 'cw'], [1, 'ccw'],
                           [4, 'cw'], [4, 'ccw']]

  # Make each possible move and return each moved puzzle
  def neighbors(self, puzzle):
    puzzles = []

    for move in self.possible_moves:
      # Necessary as python only copy location of object
      puzzle_cpy = copy.deepcopy(puzzle)
      puzzle_cpy.move(move[0], move[1])
      puzzles.append(puzzle_cpy)

    return zip(puzzles, self.possible_moves)

  # Edited implementation from
  # http://www.redblobgames.com/pathfinding/a-star/implementation.html
  def a_star(self, start):
    frontier = []
    # Sorted using f scores
    heappush(frontier, (0, start))
    came_from = {}
    # Contains g scores of all states
    cost_so_far = {}
    final_state = None

    came_from[start] = None
    cost_so_far[start] = 0

    nodes_expanded = 0

    # Helper function to determine if we have reached the state before
    def contains(state):
      for key in cost_so_far.keys():
        # Check to see if state equals to any previously visited states
        if key.equal(state):
          return key

      return 0
 
    # Helper function to determine if state has less cost than what we have
    # seen so far
    def costs_less(state, cost):
      past_state = contains(state)
      # This means we haven't visited this state before
      if past_state == 0: return True 
      return True if cost < cost_so_far[past_state] else False

    while len(frontier):
      (p_priority, p_state) = heappop(frontier)
      nodes_expanded += 1

      if p_state.is_solved():
        final_state = p_state
        break

      # Loop through each neighbor (children) of the parent node
      for (c_state, c_move) in self.neighbors(p_state):
        # The new node will have cost of its parent + 1, as we just did a
        # move to get to the child node
        new_cost = cost_so_far[p_state] + 1

        # If we haven't been to this state or if the new way of getting to
        # the state has less cost than before
        if costs_less(c_state, new_cost):
          # Record new cost
          cost_so_far[c_state] = new_cost

          # Record parent node of child node
          came_from[c_state] = p_state

          # Number used to rank items in frontier. Lower the better
          # f = g + h
          priority = new_cost + c_state.dist_heuristic()

          heappush(frontier, (priority, c_state))

    return final_state, came_from, cost_so_far, nodes_expanded

  # This should only be called after A* has correctly solve all parts of the
  # puzzle except for the edge rotation pieces.
  def fix_edges(self, puzzle):
    # The case when edge pieces are like '\'
    if puzzle.lat_edges[0] in [60, 240]:
      puzzle.move(4, 'ccw')
      puzzle.move(4, 'ccw')
      puzzle.move(4, 'ccw')
      puzzle.move(4, 'ccw')

    # The case when edge pieces are like '/'
    elif puzzle.lat_edges[0] in [120, 300]:
      puzzle.move(4, 'cw')
      puzzle.move(4, 'cw')
      puzzle.move(4, 'cw')
      puzzle.move(4, 'cw')

    else:
      pass

    if puzzle.lon_edges[0] in [60, 240]:
      puzzle.move(0, 'ccw')
      puzzle.move(0, 'ccw')
      puzzle.move(0, 'ccw')
      puzzle.move(0, 'ccw')

    elif puzzle.lon_edges[0] in [120, 300]:
      puzzle.move(0, 'cw')
      puzzle.move(0, 'cw')
      puzzle.move(0, 'cw')
      puzzle.move(0, 'cw')

    else:
      pass

    if puzzle.cut_edges[0] in [60, 240]:
      puzzle.move(1, 'ccw')
      puzzle.move(1, 'ccw')
      puzzle.move(1, 'ccw')
      puzzle.move(1, 'ccw')

    elif puzzle.cut_edges[0] in [120, 300]:
      puzzle.move(1, 'cw')
      puzzle.move(1, 'cw')
      puzzle.move(1, 'cw')
      puzzle.move(1, 'cw')

    else:
      pass
    
    return puzzle
