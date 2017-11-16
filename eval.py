import matplotlib.pyplot as plt

for i in [1,2,3,4,5]:
  x = []
  y = []

  with open('./%d.csv' % i, 'r') as f:
    for line in f:
      tokens = line.strip().split(',')
      x.append(int(tokens[1]))
      y.append(float(tokens[2]))

    plt.plot(x, y, label='Trial %d' % i)

plt.legend()
plt.xlabel('Number of iterations')
plt.ylabel('B count / num iters')
plt.title('MCMC P(B|C=T)')
plt.savefig('figure.png')
