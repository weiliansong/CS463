import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Visualizer:

  def __init__(self):
    fig, axes = plt.subplots()
    self.fig = fig
    self.axes = axes

  # 0 Blue
  # 1 Yellow
  # 2 Green
  # 3 Orange
  # 4 Red
  # 5 Purple
  def visualize(self, puzzle):
    print('lat edges', puzzle.lat_edges)
    print('lon edges', puzzle.lon_edges)
    print('cut edges', puzzle.cut_edges)
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

    # import ipdb; ipdb.set_trace()
    self.axes.matshow(cross, cmap=cmap)
    self.axes.axis('off')
    self.fig.show()
    plt.pause(1)
