import copy
import numpy as np

from heapq import heappush, heappop

class Solver:

  def __init__():
    # All possible moves
    self.possible_moves = [[0, 'cw'], [0, 'ccw'],
                           [1, 'cw'], [1, 'ccw'],
                           [4, 'cw'], [4, 'ccw']]

  # LOL this seems too easy... 
  def loss(puzzle):
    loss = 0

    for middle, face in enumerate(puzzle.ball):
      # middle is the center color of the face
      loss += np.count_nonzero(face - idx)

    loss += np.count_nonzero(puzzle.lat_edges)
    loss += np.count_nonzero(puzzle.lon_edges)
    loss += np.count_nonzero(puzzle.cut_edges)

    return int(loss / 36)

  def neighbors(puzzle):
    puzzles = []

    for move in self.possible_moves:
      puzzle_cpy = copy.deepcopy(puzzle)
      puzzle_cpy.move(move[0], move[1])
      puzzles.append(puzzle_cpy)

    return zip(puzzles, self.possible_moves)

  # Implemented with inspiration from
  # http://www.redblobgames.com/pathfinding/a-star/implementation.html
  def a_star(puzzle):
    frontier = []
    path = {}
    cost_so_far = {}

    path[puzzle] = None
    cost_so_far[puzzle] = 0

    # Insert first node here
    heappush(frontier, (0, puzzle))

    while len(frontier):
      current = heappop(frontier)

      if loss(current) == 0:
        break

    for (state, move) in neighbors(puzzle):
      new_cost = cost_so_far[puzzle] + 1

      if state not in cost_so_far or new_cost < cost_so_far[puzzle]:
        cost_so_far[state] = new_cost
        priority = new_cost + loss(state)
        heappush(frontier, (priority, state))
        path[state] = puzzle

    return path, cost_so_far
