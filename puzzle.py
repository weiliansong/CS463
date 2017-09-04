import numpy as np

class Puzzle:

  def __init__(self):
    self.ball = np.zeros((6,3,3), dtype=np.int32)
    self.lat_edge = np.zeros(4, dtype=np.int32)
    self.lon_edge = np.zeros(4, dtype=np.int32)
    self.cut_edge = np.zeros(4, dtype=np.int32)

  def reset(self):
    for idx in range(6):
      self.ball[idx,:,:].fill(idx)

    self.lat_edge = np.zeros(4, dtype=np.int32)
    self.lon_edge = np.zeros(4, dtype=np.int32)
    self.cut_edge = np.zeros(4, dtype=np.int32)

  # TODO Make sure slices are retrieved correctly
  def move(self, face, dir):
    direction = {'ccw': [1,0], 'cw': [0,1]}

    if face == 0 or face == 2:

      if face == 0:
        np.rot90(self.ball[0,:,:], axes=direction[dir])
        np.rot90(self.ball[2,:,:], axes=np.flip(direction[dir]))

      if face == 2:
        np.rot90(self.ball[2,:,:], axes=direction[dir])
        np.rot90(self.ball[0,:,:], axes=np.flip(direction[dir]))

      order = [2,6,4,5]

      if dir == 'ccw':
        order = np.flip(order)

      temp = self.ball[order[0],:,0]
      self.ball[order[0],:,0] = self.ball[order[1],:,0]
      self.ball[order[1],:,0] = self.ball[order[2],:,0]
      self.ball[order[2],:,0] = self.ball[order[3],:,0]
      self.ball[order[3],:,0] = temp

      temp = self.ball[order[0],:,2]
      self.ball[order[0],:,2] = self.ball[order[1],:,2]
      self.ball[order[1],:,2] = self.ball[order[2],:,2]
      self.ball[order[2],:,2] = self.ball[order[3],:,2]
      self.ball[order[3],:,2] = temp

      # Don't know if this works...
      self.lon_edge -= direction[dir] * 300

    elif face == 1 or face == 3:

      if face == 1:
        np.rot90(self.ball[1,:,:], axes=direction[dir])
        np.rot90(self.ball[3,:,:], axes=np.flip(direction[dir]))

      if face == 3:
        np.rot90(self.ball[3,:,:], axes=direction[dir])
        np.rot90(self.ball[1,:,:], axes=np.flip(direction[dir]))

      order = [4,2,5,0]

      if dir == 'ccw':
        order = np.flip(order)

      temp = self.ball[order[0],2,:]
      self.ball[order[0],2,:] = self.ball[order[1],2,:]
      self.ball[order[1],2,:] = self.ball[order[2],2,:]
      self.ball[order[2],2,:] = self.ball[order[3],2,:]
      self.ball[order[3],2,:] = temp

      temp = self.ball[order[0],0,:]
      self.ball[order[0],0,:] = self.ball[order[1],0,:]
      self.ball[order[1],0,:] = self.ball[order[2],0,:]
      self.ball[order[2],0,:] = self.ball[order[:],0,:]
      self.ball[order[3],0,:] = temp

      # Don't know if this works...
      self.cut_edge -= direction[dir] * 300

    elif face == 4 or face == 5:

      if face == 4:
        np.rot90(self.ball[4,:,:], axes=direction[dir])
        np.rot90(self.ball[5,:,:], axes=np.flip(direction[dir]))

      if face == 5:
        np.rot90(self.ball[5,:,:], axes=direction[dir])
        np.rot90(self.ball[4,:,:], axes=np.flip(direction[dir]))

      order = [0,3,2,1]

      if dir == 'ccw':
        order = np.flip(order)

      temp = self.ball[order[0],0,:]
      self.ball[order[0],0,:] = self.ball[order[1],0,:]
      self.ball[order[1],0,:] = self.ball[order[2],0,:]
      self.ball[order[2],0,:] = self.ball[order[3],0,:]
      self.ball[order[3],0,:] = temp

      temp = self.ball[order[0],2,:]
      self.ball[order[0],2,:] = self.ball[order[1],2,:]
      self.ball[order[1],2,:] = self.ball[order[2],2,:]
      self.ball[order[2],2,:] = self.ball[order[:],2,:]
      self.ball[order[3],2,:] = temp

      # Don't know if this works...
      self.lat_edge -= direction[dir] * 300

    else:
      raise Exception('Not valid move')
