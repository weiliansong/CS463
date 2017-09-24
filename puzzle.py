import numpy as np

class Puzzle:

  def __init__(self):
    self.ball = np.zeros((6,3,3), dtype=np.int32)
    self.lat_edges = np.zeros(4, dtype=np.int32)
    self.lon_edges = np.zeros(4, dtype=np.int32)
    self.cut_edges = np.zeros(4, dtype=np.int32)

    self.ball_3d = np.zeros((3,3,3), dtype='3int8')

    for i in range(3):
      for j in range(3):
        for k in range(3):
          self.ball_3d[i,j,k] = [i,j,k]

    self.reset()

  def __str__(self):
    name = 'puzzle_loss: ' + str(self.loss())
    return name

  def __lt__(self, other):
    return self.dist_heuristic() < other.dist_heuristic()

  def equal(self, other):
    difference = 0
    difference += np.count_nonzero(self.ball - other.ball)
    difference += np.count_nonzero(self.lat_edges - other.lat_edges)
    difference += np.count_nonzero(self.lon_edges - other.lon_edges)
    difference += np.count_nonzero(self.cut_edges - other.cut_edges)

    return not difference

  def manhattan(self, p1, p2):
    return np.abs(p1[0]-p2[0]) + np.abs(p1[1]-p2[1]) + np.abs(p1[2]-p2[2])

  def dist_heuristic(self):
    edges = 0
    corners = 0

    # Edges first
    for i in [0,1,2]:
      for j in [[0,1], [1,0], [1,2], [2,1]]:
        x = i
        y, z = j
        
        edges += self.manhattan((x,y,z), self.ball_3d[x,y,z])

    # Corners next
    for i in [0,2]:
      for j in [0,2]:
        for k in [0,2]:
          corners += self.manhattan((x,y,z), self.ball_3d[x,y,z])

    return max(edges/8, corners/8)

  def is_solved(self):
    pieces_wrong = 0.0

    for middle, face in enumerate(self.ball):
      pieces_wrong += np.count_nonzero(face - middle)

    return not pieces_wrong

  def reset(self):
    for idx in range(6):
      self.ball[idx,:,:].fill(idx)

    self.lat_edges = np.zeros(4, dtype=np.int32)
    self.lon_edges = np.zeros(4, dtype=np.int32)
    self.cut_edges = np.zeros(4, dtype=np.int32)

    for i in range(3):
      for j in range(3):
        for k in range(3):
          self.ball_3d[i,j,k] = [i,j,k]

  # 0 Left
  # 1 Front
  # 2 Right
  # 3 Back
  # 4 Top
  # 5 Bottom
  def move(self, face, dir):
    direction = {'cw': [1,0], 'ccw': [0,1]}

    if face == 0:
      # Rotate 3D matrix
      self.ball_3d[:,:,0] = np.rot90(self.ball_3d[:,:,0], axes=direction[dir])
      self.ball_3d[:,:,2] = np.rot90(self.ball_3d[:,:,2], axes=direction[dir])

      self.ball[0,:,:] = np.rot90(self.ball[0,:,:], axes=direction[dir])
      self.ball[2,:,:] = np.rot90(self.ball[2,:,:], axes=direction[dir])

      if dir == 'ccw':
        order = [4,1,5,3]

        temp = np.copy(self.ball[order[0],:,0])
        self.ball[order[0],:,0] = np.copy(self.ball[order[1],:,0]) 
        self.ball[order[1],:,0] = np.copy(self.ball[order[2],:,0])
        self.ball[order[2],:,0] = np.copy(self.ball[order[3],:,0])
        self.ball[order[3],:,0] = temp

        temp = np.copy(self.ball[order[0],:,2])
        self.ball[order[0],:,2] = np.copy(self.ball[order[3],:,2]) 
        self.ball[order[3],:,2] = np.copy(self.ball[order[2],:,2])
        self.ball[order[2],:,2] = np.copy(self.ball[order[1],:,2])
        self.ball[order[1],:,2] = temp

      elif dir == 'cw':
        order = [4,3,5,1]

        temp = np.copy(self.ball[order[0],:,0])
        self.ball[order[0],:,0] = np.copy(self.ball[order[1],:,0]) 
        self.ball[order[1],:,0] = np.copy(self.ball[order[2],:,0])
        self.ball[order[2],:,0] = np.copy(self.ball[order[3],:,0])
        self.ball[order[3],:,0] = temp

        temp = np.copy(self.ball[order[0],:,2])
        self.ball[order[0],:,2] = np.copy(self.ball[order[3],:,2]) 
        self.ball[order[3],:,2] = np.copy(self.ball[order[2],:,2])
        self.ball[order[2],:,2] = np.copy(self.ball[order[1],:,2])
        self.ball[order[1],:,2] = temp

      else:
        raise Exception('Not a valid move')

      self.lon_edges += [300, 300, 300, 300] * np.diff(direction[dir])
      self.lon_edges = np.mod(self.lon_edges, 360)

      # Copy lat edge for copying
      cpy_edges = np.copy(self.lat_edges)

      if dir == 'cw':
        self.lat_edges[0] = self.cut_edges[1]
        self.lat_edges[1] = self.cut_edges[0]
        self.lat_edges[2] = self.cut_edges[2]
        self.lat_edges[3] = self.cut_edges[3]

        self.cut_edges[0] = cpy_edges[0]
        self.cut_edges[1] = cpy_edges[1]
        self.cut_edges[2] = cpy_edges[3]
        self.cut_edges[3] = cpy_edges[2]

      else:
        self.lat_edges[0] = self.cut_edges[0]
        self.lat_edges[1] = self.cut_edges[1]
        self.lat_edges[2] = self.cut_edges[3]
        self.lat_edges[3] = self.cut_edges[2]

        self.cut_edges[0] = cpy_edges[1]
        self.cut_edges[1] = cpy_edges[0]
        self.cut_edges[2] = cpy_edges[2]
        self.cut_edges[3] = cpy_edges[3]


    elif face in [1]:
      # Rotate 3D matrix
      self.ball_3d[:,2,:] = np.rot90(self.ball_3d[:,2,:], axes=direction[dir])
      self.ball_3d[:,0,:] = np.rot90(self.ball_3d[:,0,:], axes=direction[dir])

      self.ball[1,:,:] = np.rot90(self.ball[1,:,:], axes=direction[dir])
      self.ball[3,:,:] = np.rot90(self.ball[3,:,:], axes=direction[dir])

      if dir == 'ccw':
        order = [0,4,2,5]

        temp = np.copy(self.ball[order[0],2,:])
        self.ball[order[0],2,:] = np.copy(self.ball[order[1],2,:]) 
        self.ball[order[1],2,:] = np.copy(self.ball[order[2],2,:])
        self.ball[order[2],2,:] = np.flip(self.ball[order[3],0,:], axis=0)
        self.ball[order[3],0,:] = temp

        temp = np.copy(self.ball[order[0],0,:])
        self.ball[order[0],0,:] = np.flip(self.ball[order[3],2,:], axis=0) 
        self.ball[order[3],2,:] = np.copy(self.ball[order[2],0,:])
        self.ball[order[2],0,:] = np.copy(self.ball[order[1],0,:])
        self.ball[order[1],0,:] = temp

      elif dir == 'cw':
        order = [0,5,2,4]

        temp = np.copy(self.ball[order[0],2,:])
        self.ball[order[0],2,:] = np.flip(self.ball[order[1],0,:], axis=0) 
        self.ball[order[1],0,:] = np.copy(self.ball[order[2],2,:])
        self.ball[order[2],2,:] = np.copy(self.ball[order[3],2,:])
        self.ball[order[3],2,:] = temp

        temp = np.copy(self.ball[order[0],0,:])
        self.ball[order[0],0,:] = np.copy(self.ball[order[3],0,:]) 
        self.ball[order[3],0,:] = np.copy(self.ball[order[2],0,:])
        self.ball[order[2],0,:] = np.flip(self.ball[order[1],2,:], axis=0)
        self.ball[order[1],2,:] = temp

      else:
        raise Exception('Not a valid move')

      self.cut_edges += [300, 300, 300, 300] * np.diff(direction[dir])
      self.cut_edges = np.mod(self.cut_edges, 360)

      cpy_edges = np.copy(self.lon_edges)

      if dir == 'cw':
        self.lon_edges[0] = self.lat_edges[3]
        self.lon_edges[1] = self.lat_edges[0]
        self.lon_edges[2] = self.lat_edges[2]
        self.lon_edges[3] = self.lat_edges[1]

        self.lat_edges[0] = cpy_edges[0]
        self.lat_edges[1] = cpy_edges[2]
        self.lat_edges[2] = cpy_edges[3]
        self.lat_edges[3] = cpy_edges[1]

      else:
        self.lon_edges[0] = self.lat_edges[0]
        self.lon_edges[1] = self.lat_edges[3]
        self.lon_edges[2] = self.lat_edges[1]
        self.lon_edges[3] = self.lat_edges[2]

        self.lat_edges[0] = cpy_edges[2]
        self.lat_edges[1] = cpy_edges[0]
        self.lat_edges[2] = cpy_edges[1]
        self.lat_edges[3] = cpy_edges[3]

    elif face in [4]:
      # Rotate 3D matrix
      self.ball_3d[0,:,:] = np.rot90(self.ball_3d[0,:,:], axes=direction[dir])
      self.ball_3d[2,:,:] = np.rot90(self.ball_3d[2,:,:], axes=direction[dir])

      self.ball[4,:,:] = np.rot90(self.ball[4,:,:], axes=direction[dir])
      self.ball[5,:,:] = np.rot90(self.ball[5,:,:], axes=direction[dir])

      if dir == 'ccw':
        order = [0,3,2,1]

        temp = np.copy(self.ball[order[0],:,2])
        self.ball[order[0],:,2] = np.flip(self.ball[order[1],2,:], axis=0) 
        self.ball[order[1],2,:] = np.copy(self.ball[order[2],:,0])
        self.ball[order[2],:,0] = np.flip(self.ball[order[3],0,:], axis=0)
        self.ball[order[3],0,:] = temp

        temp = np.copy(self.ball[order[0],:,0])
        self.ball[order[0],:,0] = np.copy(self.ball[order[3],2,:]) 
        self.ball[order[3],2,:] = np.copy(self.ball[order[2],:,2])
        self.ball[order[2],:,2] = np.copy(self.ball[order[1],0,:])
        self.ball[order[1],0,:] = temp

      elif dir == 'cw':
        order = [0,1,2,3]

        temp = np.copy(self.ball[order[0],:,2])
        self.ball[order[0],:,2] = np.copy(self.ball[order[1],0,:]) 
        self.ball[order[1],0,:] = np.copy(self.ball[order[2],:,0])
        self.ball[order[2],:,0] = np.copy(self.ball[order[3],2,:])
        self.ball[order[3],2,:] = temp

        temp = np.copy(self.ball[order[0],:,0])
        self.ball[order[0],:,0] = np.flip(self.ball[order[3],0,:], axis=0) 
        self.ball[order[3],0,:] = np.copy(self.ball[order[2],:,2])
        self.ball[order[2],:,2] = np.flip(self.ball[order[1],2,:], axis=0)
        self.ball[order[1],2,:] = temp

      else:
        raise Exception('Not a valid move')

      self.lat_edges += [300, 300, 300, 300] * np.diff(direction[dir])
      self.lat_edges = np.mod(self.lat_edges, 360)

      cpy_edges = np.copy(self.cut_edges)

      if dir == 'cw':
        self.cut_edges[0] = self.lon_edges[3]
        self.cut_edges[1] = self.lon_edges[1]
        self.cut_edges[2] = self.lon_edges[2]
        self.cut_edges[3] = self.lon_edges[0]

        self.lon_edges[0] = cpy_edges[0]
        self.lon_edges[1] = cpy_edges[2]
        self.lon_edges[2] = cpy_edges[1]
        self.lon_edges[3] = cpy_edges[3]

      else:
        self.lon_edges[0] = self.lat_edges[1]
        self.lon_edges[1] = self.lat_edges[3]
        self.lon_edges[2] = self.lat_edges[0]
        self.lon_edges[3] = self.lat_edges[2]

        self.lat_edges[0] = cpy_edges[2]
        self.lat_edges[1] = cpy_edges[0]
        self.lat_edges[2] = cpy_edges[3]
        self.lat_edges[3] = cpy_edges[1]
