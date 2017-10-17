test = {}

for i in range(100):
  test[i] = 0

lol = []

for i in range(100):
  lol.append(test.copy())

print(lol)
