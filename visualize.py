import glob
import numpy as np
import matplotlib.pyplot as plt

walksat_csv = glob.glob('./stats/*.csv')

walksat_data = {}

for csv_f in walksat_csv:
  sat_id = csv_f.strip().split('/')[-1]
  sat_id = sat_id.split('.')[0]
  sat_id = int(sat_id.split('_')[-1])

  f = open(csv_f, 'r')
  f_lines = f.readlines()
  f.close()

  if not f_lines:
    continue

  fitnesses = []
  times = []

  for line in f_lines[1:]:
    fitness, time = line.strip().split(',')

    fitnesses.append(int(fitness))
    times.append(float(time))

  walksat_data[sat_id] = {}
  walksat_data[sat_id]['fitness'] = max(fitnesses)
  walksat_data[sat_id]['runtime'] = np.average(times)

x = np.array(walksat_data.keys())
y = np.array([walksat_data[x_i]['runtime'] for x_i in x])

sort_idx = np.argsort(y)[::-1]
labels = x[sort_idx][:100]
y = y[sort_idx][:100]

plt.plot(range(len(y)), y)
plt.xticks(range(len(y)), labels, rotation=90)
plt.subplots_adjust(bottom=0.15)
plt.tight_layout()
plt.show()
