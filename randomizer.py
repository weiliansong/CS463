import numpy as np

class Randomizer:

  def __init__(self):
    self.past_move = [-1, 0]
    self.move_counter = 0

  def get_random_face(self):
    faces = [0, 1, 4]

    return np.random.choice(faces)

  # CW = 1, CCW = -1
  def get_random_dir(self):
    directions = [1, -1]    

    return np.random.choice(directions)

  def add_move(self, move):
    if len(self.past_moves) >= 6:
      self.past_moves.pop()

    self.past_moves.add(move)

  def get_random_move(self):
    move = [self.get_random_face(), self.get_random_dir()]

    while True:
      if move[0] == self.past_move[0]:
        if move[1] == self.past_move[1]:
          if self.move_counter < 6:
            self.move_counter += 1
            break

        elif move[1] == -self.past_move[1]:
          pass

      else:
        self.move_counter = 0
        break

      move = [self.get_random_face(), self.get_random_dir()]

    if move[1] == -1:
      move = (move[0], 'ccw')
      
    else:
      move = (move[0], 'cw')

    return move
