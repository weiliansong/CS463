import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Visualizer:

  def __init__(self):
    self.rot_key = {
      120: '/',
      300: '/',
      60:  '\\',
      240: '\\',
      0:   '-',
      180: '-'
    }

  def visualize(self, puzzle):
    fig, axes = plt.subplots()

    print('lat edges')
    print([self.rot_key[x] + ' ' for x in puzzle.lat_edges])

    print('lon edges')
    print([self.rot_key[x] + ' ' for x in puzzle.lon_edges])

    print('cut edges')
    print([self.rot_key[x] + ' ' for x in puzzle.cut_edges])

    print('\n')

    cross = np.zeros((12,9), np.float32)
    cross.fill(-1)

    cross[0:3, 3:6]  = puzzle.ball[3]
    cross[3:6, 0:3]  = puzzle.ball[0]
    cross[3:6, 3:6]  = puzzle.ball[4]
    cross[3:6, 6:9]  = puzzle.ball[2]
    cross[6:9, 3:6]  = puzzle.ball[1]
    cross[9:12, 3:6] = puzzle.ball[5]

    cmap = mcolors.LinearSegmentedColormap.from_list('mycmap', 
        ['white', 'blue', 'yellow', 'green', 'orange', 'purple', 'red'])

    axes.matshow(cross, cmap=cmap)
    axes.axis('off')
    fig.show()
    plt.pause(1)
