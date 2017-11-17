import probs

# Random assignment
book = {
  'A': probs.coin_flip(0.5),
  'B': probs.coin_flip(0.5),
  'C': 1,
  'D': probs.coin_flip(0.5),
  'E': probs.coin_flip(0.5),
}

b_count = 0

for i in range(1,10001):
  # Update the variables
  book['A'] = probs.A(book['B'], book['C'], book['D'])
  book['D'] = probs.D(book['A'], book['C'], book['E'])
  book['E'] = probs.E(book['C'], book['D'])
  book['B'] = probs.B(book['A'])

  if book['B']:
    b_count += 1

  if (i % 1000) == 0:
    print('%d,%d,%f' % (b_count, i, float(b_count)/float(i)))
