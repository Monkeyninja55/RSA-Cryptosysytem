# Kush Patel
# CMSC 441
# Project 2 part1a
# RSA Implementation; may take up to 30 seconds for 1024 bits

import sys
import random


# Encodes message as an integer
def signMess():
  M = "I deserve an A"
  y = 0

  for i in range(0, len(M)):
    y += ord(M[i]) << (8 * (len(M) - 1 - i))
  return y


# Extended Euclidean for calculating modular inverses
def moduInv(a, b):
  if b == 0:
    return (a, 1, 0)

  else:
    d, x1, y1 = moduInv(b, a % b)
    x = y1
    y = x1 - ((a//b) * y1)
    return (d, x, y)


# Determines if n is composite with a as a witness
def witness(a, n):
  u = n - 1
  t = 0
  x = []

  while (u % 2) == 0:
    u //= 2
    t += 1

  x.append(pow(a, u, n))
  if x[len(x) - 1] == 1:
    return False

  for i in range(1, t):
    x.append(pow(x[len(x) - 1], 2, n))
    if (x[len(x) - 1] == 1) and (x[len(x) - 2] != 1) and (x[len(x) - 2] != n - 1):
      return True

  x.append(pow(x[len(x) - 1], 2, n))
  if x[len(x) - 1] != 1:
    return True
  return False


# Miller-Rabin primality test
def millRab(n):
  if (n <= 2) or (n % 2 == 0):
    return False

  for i in range(0, 10):
    a = random.randrange(1, n - 1)
    w = witness(a, n)
    if w == True:
      return False
  return True


def main():
  num = 0
  checkP = False
  checkQ = False

  # 1024 bits may take up to 30 seconds
  while num < 6:
    num = int(input('Please enter a modulus size greater than 5: '))

  # Takes care of odd bits
  if (num % 2) != 0:
    num //= 2

  # Keeps generating numbers until p is prime
  while checkP == False:
    p = random.getrandbits(num)
    checkP = millRab(p)

  q = p
  # Makes sure p != q, and q is prime
  while (checkQ == False) or (p == q):
    q = random.getrandbits(num)
    checkQ = millRab(q)

  # Chose 65537 since it's relatively prime to phi(n) for 1024 bits
  e = 65537
  n = p * q
  phi = (p - 1) * (q - 1)

  d, x, y = moduInv(e, phi)
  d = x % phi

  M = signMess()
  SM = pow(M, d, n)

  # For writing output to file
  #sys.stdout = open('output.txt', 'w')

  sys.stdout.write('\n****RSA public key****\n')
  sys.stdout.write('e value: ' + str(e) + '\n\n')
  sys.stdout.write('n value: ' + str(n) + '\n\n')

  sys.stdout.write('****RSA secret key****\n')
  sys.stdout.write('d value: ' + str(d) + '\n\n')
  sys.stdout.write('n value: ' + str(n) + '\n\n')

  sys.stdout.write('****Signature computed with secret key****\n')
  sys.stdout.write('Signed Message value: ' + str(SM) + '\n\n')


main()
