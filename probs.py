import numpy as np

def coin_flip(pos_prob):
  return np.random.choice([0,1], p=[1.0-pos_prob, pos_prob])

def A(B,C,D):
  if B and C and D:
    return coin_flip(0.8873)

  elif not B and C and not D:
    return coin_flip(0.8571)

  elif B and C and not D:
    return coin_flip(0.9921)

  elif not B and C and D:
    return coin_flip(0.2727)

  else:
    raise Exception('A prob not found')

def B(A):
  if A:
    return coin_flip(0.7)

  elif not A:
    return coin_flip(0.1)

  else:
    raise Exception('B prob not found')

def D(A,C,E):
  if A and C and E:
    return coin_flip(0.027)

  elif not A and C and not E:
    return coin_flip(0.973)

  elif A and C and not E:
    return coin_flip(0.6923)

  elif not A and C and E:
    return coin_flip(0.3077)

  else:
    raise Exception('D prob not found')

def E(C,D):
  if C and D:
    return coin_flip(0.1)

  elif C and not D:
    return coin_flip(0.9)

  else:
    raise Exception('E prob not found')
