from puzzle import Puzzle
from visualizer import Visualizer
from randomizer import Randomizer

ball = Puzzle()
cross = Visualizer()
rand = Randomizer()

moves = []

# Asks user for number of random moves
num_moves = int(input('How many random moves: '))

for idx in range(num_moves):
  moves.append(rand.get_random_move())

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

for move in moves:
  print(move)

# 0, 1, 4 only
for move in moves:
  ball.move(move[0], move[1])
  cross.visualize(ball)
