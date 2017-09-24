import time
from solver import Solver
from puzzle import Puzzle
from visualizer import Visualizer
from randomizer import Randomizer

puzzle = Puzzle()
visualizer = Visualizer()
rand = Randomizer()
solver = Solver()

puzzle.move(1, 'ccw')
puzzle.move(0, 'cw')
puzzle.move(4, 'ccw')
puzzle.move(1, 'cw')
puzzle.move(0, 'ccw')
puzzle.move(4, 'cw')
# puzzle.move(1, 'ccw')
# puzzle.move(0, 'cw')
# puzzle.move(4, 'cw')

# moves = []

# Asks user for number of random moves
# num_moves = int(input('How many random moves: '))
# 
# for idx in range(num_moves):
#   moves.append(rand.get_random_move())

start = time.time()
final_state, came_from, cost_so_far = solver.a_star(puzzle)
end = time.time()

print(end-start)
visualizer.visualize(final_state)

# moves.append([1, 'ccw'])
# moves.append([1, 'ccw'])
# moves.append([4, 'cw'])
# moves.append([0, 'ccw'])
# moves.append([4, 'ccw'])
# moves.append([0, 'ccw'])
# moves.append([0, 'ccw'])
# moves.append([4, 'ccw'])
# moves.append([1, 'cw'])
# moves.append([4, 'cw'])

# for move in moves:
#   print(move)
# 
# # 0, 1, 4 only
# for move in moves:
#   ball.move(move[0], move[1])
#   cross.visualize(ball)
