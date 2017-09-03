import numpy as np

class Puzzle:

    def __init__(self):
        self.ball = np.zeros((3,3,3), dtype=np.int32)
        self.center_edge = np.zeros((3,3,3), dtype=np.int32)

    def reset(self):
        self.ball = np.arange(27).reshape((3,3,3))
        self.center_edge = np.zeros((3,3,3), dtype=np.int32)

    # TODO Make sure slices are retrieved correctly
    def move(self, face, dir):
        direction = {'ccw': [1,0], 'cw': [0,1]}

        if face == 'left':
            slice = self.ball[:,:,0]
            self.ball[:,:,0] = np.rot90(slice, axes=direction[dir])
            self.center_edge[:,:,1] += np.diff(direction[dir]) * 300
            self.center_edge[:,:,1] = np.mod(self.center_edge[:,:,1], 360)

        elif face == 'right':
            slice = self.ball[:,:,2]
            self.ball[:,:,2] = np.rot90(slice, axes=direction[dir])
            self.center_edge[:,:,1] += np.diff(direction[dir]) * 300
            self.center_edge[:,:,1] = np.mod(self.center_edge[:,:,1], 360)

        elif face == 'top':
            slice = self.ball[0,:,:]
            self.ball[0,:,:] = np.rot90(slice, axes=direction[dir])
            self.center_edge[1,:,:] += np.diff(direction[dir]) * 300
            self.center_edge[1,:,:] = np.mod(self.center_edge[:,:,1], 360)

        elif face == 'bottom':
            slice = self.ball[2,:,:]
            self.ball[2,:,:] = np.rot90(slice, axes=direction[dir])
            self.center_edge[1,:,:] += np.diff(direction[dir]) * 300
            self.center_edge[1,:,:] = np.mod(self.center_edge[:,:,1], 360)

        elif face == 'back':
            slice = self.ball[:,0,:]
            self.ball[:,0,:] = np.rot90(slice, axes=direction[dir])
            self.center_edge[:,1,:] += np.diff(direction[dir]) * 300
            self.center_edge[:,1,:] = np.mod(self.center_edge[:,:,1], 360)

        elif face == 'front':
            slice = self.ball[:,2,:]
            self.ball[:,2,:] = np.rot90(slice, axes=direction[dir])
            self.center_edge[:,1,:] += np.diff(direction[dir]) * 300
            self.center_edge[:,1,:] = np.mod(self.center_edge[:,:,1], 360)

        else:
            raise Exception('Not valid move')

    def print_layers(self):
        for idx, layer in enumerate(self.ball):
            print(idx)
            print(layer)

        for idx, layer in enumerate(self.center_edge):
            print(idx, 'center edge')
            print(layer)

    def test(self):
        self.reset()
        self.print_layers()
        self.move('right', 'cw')
        self.print_layers()
        print('\n')

        self.move('right', 'cw')
        self.print_layers()
        print('\n')

        self.move('right', 'cw')
        self.print_layers()
        print('\n')

        self.move('right', 'cw')
        self.print_layers()
        print('\n')
