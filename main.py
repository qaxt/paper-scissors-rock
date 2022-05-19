# Paper Scissors Rock in 8 Lines
import random
def check(p, c):
  if (p == c):
    return 'draw'
  if (p == c + 1 or p == c - 2):
    return 'win'
  return 'lose'
print(check(int(input('0 for paper, 1 for scissors, 2 for rock\n')), random.randint(0, 3)))

# Losing Cases
print(check(0, 1))
print(check(1, 2))
print(check(2, 0))

# Winning Cases
print(check(0, 2))
print(check(1, 0))
print(check(2, 1))