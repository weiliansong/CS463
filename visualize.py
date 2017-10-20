import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def grab_data(csv_files):
  data = {}

  for csv_f in csv_files:
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

    data[sat_id] = {}
    data[sat_id]['fitness'] = max(fitnesses)
    data[sat_id]['runtime'] = np.average(times)

  return data

def plot(labels, values, plt_title, y_label):
  assert len(labels) == len(values)

  sort_idx = np.argsort(values)[::-1]
  labels = labels[sort_idx]
  values = values[sort_idx]

  split_labels = np.array_split(labels, 3)
  split_values = np.array_split(values, 3)

  plot_datas = zip(split_labels, split_values)

  for plot_idx, (_labels, _values) in enumerate(plot_datas):
    fig = plt.figure(figsize=(20,10), dpi=80)
    ax = fig.add_subplot(111)
    ax.plot(range(len(_values)), _values)
    plt.xticks(range(len(_labels)), _labels, rotation=90)
    plt.xlabel('Algorithm ID')
    plt.ylabel(y_label)
    plt.title('%s %d' % (plt_title, plot_idx+1))
    plt.tight_layout()
    fig.savefig('./visualizations/%s_%d.png' % (plt_title, plot_idx+1))
    plt.clf()

walksat_data = grab_data(glob.glob('./stats_WalkSAT/100_*.csv'))
genetic_data = grab_data(glob.glob('./stats_Genetic/100_*.csv'))
dpll_data    = grab_data(glob.glob('./stats_DPLL/100_*.csv'))

if not os.path.exists('./visualizations'):
  os.mkdir('./visualizations')

# WalkSAT plotting
labels = np.array(walksat_data.keys())
runtimes = np.array([walksat_data[label]['runtime'] for label in labels])
fitnesses = np.array([walksat_data[label]['fitness'] for label in labels])
plot(labels, runtimes, 'WalkSAT_Runtime', 'Runtime (s)')
plot(labels, fitnesses, 'WalkSAT_Fitnesses', 'Fitness (# clauses)')

# Genetic plotting
labels = np.array(genetic_data.keys())
runtimes = np.array([genetic_data[label]['runtime'] for label in labels])
fitnesses = np.array([genetic_data[label]['fitness'] for label in labels])
plot(labels, runtimes, 'Genetic_Runtime', 'Runtime (s)')
plot(labels, fitnesses, 'Genetic_Fitnesses', 'Fitness (# clauses)')

# DPLL plotting
labels = np.array(dpll_data.keys())
runtimes = np.array([dpll_data[label]['runtime'] for label in labels])
fitnesses = np.array([dpll_data[label]['fitness'] for label in labels])
plot(labels, runtimes, 'DPLL_Runtime', 'Runtime (s)')
plot(labels, fitnesses, 'DPLL_Fitnesses', 'Fitness (# clauses)')
