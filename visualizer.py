import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Visualizer:

  def __init__(self):
    pass

  def visualize(self, puzzle):
    cross = np.zeros((12,9), np.float32)
    cross.fill(-1)

    cross[0:3, 3:6]  = puzzle.ball[3]
    cross[3:6, 0:3]  = puzzle.ball[0]
    cross[3:6, 3:6]  = puzzle.ball[5]
    cross[3:6, 6:9]  = puzzle.ball[2]
    cross[6:9, 3:6]  = puzzle.ball[1]
    cross[9:12, 3:6] = puzzle.ball[4] # Only one that's in question?

    cmap = mcolors.LinearSegmentedColormap.from_list('mycmap', 
        ['white', 'blue', 'yellow', 'green', 'orange', 'red', 'purple'])

    # import ipdb; ipdb.set_trace()
    plt.matshow(cross, cmap=cmap)
    plt.axis('off')
    plt.show()
