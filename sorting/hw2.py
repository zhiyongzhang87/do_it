# Imports
import math
import random
from datetime import datetime
import numpy as np

N = 10000

def sieve(n: int):
    is_prime = np.ones(n + 1, dtype=bool)
    # TODO: Set is_prime[0] and is_prime[1] to False
    # Then iterate over all elements and if it is True (meaning a prime)
    # mark all its multiples as False
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,n+1):
      if is_prime[i]:
        m = 2
        while i * m <= n:
          is_prime[i*m] = False
          m += 1
    primes = [i for i in range(n+1) if is_prime[i]]
    return set(primes)

primes = sieve(N)
print(len(primes))

def fermat_is_prime(p: int, base=None):
    if p == 2: return True
    if base is None:
        while True:
            base = random.randint(2, p)
            if math.gcd(p, base) == 1:
                break
    # TODO: Compute (base)^(p-1) % p. Consider using the `pow` built-in function.
    # If the result is 1, return True
    # Otherwise, return False
    # Make sure that you don't use numbers significantly bigger than `p`
    if pow(base, p-1) % p != 1:
      return False
    return True

def boosted_fermat(p: int, delta=1e-6):
    trust = 1
    while trust > delta:
        # TODO: Use the fermat primality testing multiple times to avoid pseudoprimes
        if not fermat_is_prime(p):
          return False
        trust = trust / 2
    return True

for p in range(2, N+1):
    # TODO: Find all the Carmichael numbers
    if boosted_fermat(p) and p not in primes:
      print(p)

def generate_prime(bits, verbose = False):
  start = datetime.now()

  i = 0
  while True:
      i += 1
      if verbose and i % 10 == 0:
          print(f'\rAttempting try {i:5d}. Elapsed time: {(datetime.now() - start).total_seconds():8.2f}s', end='')
      p = random.randint(pow(2,bits-1), pow(2,bits))       # TODO: Generate a number in [ 2**(bits-1), 2**(bits) )
      if boosted_fermat(p):   # TODO: Check if it is prime using the boosted fermat test you
          if verbose:
              print()  # Prevent the next line from overwriting the previous (see \r carriage return)
          return p, i

start = datetime.now()
p, i = generate_prime(32, verbose = True)
print(f'After {i} tries completed in {(datetime.now() - start).total_seconds():.2f} seconds, generated the following prime\n{p}')

# 2048 is one of the recommended prime sizes in RSA. This cell may take a minute or two.
# Feel free to test at lower numbers.

