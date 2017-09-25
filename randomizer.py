import numpy as np

class Randomizer:

  def __init__(self):
    # Records the last move we did
    self.past_move = [-1, 0]

    # Records how many of the same move we did
    self.move_counter = 0

  def get_random_face(self):
    # We only rotate these faces
    faces = [0, 1, 4]

    return np.random.choice(faces)

  # CW = 1, CCW = -1
  def get_random_dir(self):
    # We choose a random direction
    directions = [1, -1]    

    return np.random.choice(directions)

  def get_random_move(self):

    while True:
      move = [self.get_random_face(), self.get_random_dir()]

      # If we are moving the same face as we did in the last move
      if move[0] == self.past_move[0]:
        # We check if we are rotating in the same direction as well
        if move[1] == self.past_move[1]:
          # If yes, then we make sure we haven't done it more than 12 times
          if self.move_counter < 12:
            # Increment same move counter
            self.move_counter += 1
            # Remember the move we did
            self.past_move = move
            break

        # If no, then we need to discard the move as it is undoing the last
        # move we did
        elif move[1] == -self.past_move[1]:
          continue

      # If we are moving a difference face than what we did before, we know
      # this must be a valid move
      else:
        # Reset same move counter
        self.move_counter = 0
        # Remember the move we did
        self.past_move = move
        break

    # Decode direction value
    if move[1] == -1:
      move = (move[0], 'ccw')
      
    else:
      move = (move[0], 'cw')

    return move
