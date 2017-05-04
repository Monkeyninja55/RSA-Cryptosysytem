# Kush Patel
# CMSC 441
# Project 2 part2
# Pollard Rho Implementation;

import random
import fractions


def main():

  # Modulus here
  n = 3.78704518375826E+59

  x = []
  i = 1
  x1 = random.randrange(0, n - 1)

  x.append(x1)
  y = x1
  k = 2

  while True:
    i = i + 1
    xi = (pow(x[len(x) - 1], 2) - 1) % n
    x.append(xi)

    d = fractions.gcd(y - xi, n)

    # Prints factor
    if (d != 1) and (d != n):
      print('Factor', d)
      break

    if i == k:
      y = xi
      k = 2 * k
 
main()
