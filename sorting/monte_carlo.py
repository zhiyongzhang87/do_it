# monte carlo: primarily for testing
# def> a postive integer n >= 2 is prime
# if the only postive integer that divide n are 1 and n
# otherwise, n is composite
# 
# classic problem: given integer n >= 2
# is n prime?
# modern problem: generate a random n-bit integer in [1...n]
# and test if it is prime
# 
# when n goes to infinite, the numbers of primes in [1...n] is n/ln(n)
# if pick a 100-bit integer z at random
# P(z is prime) = 1/ln(2^100) = 1/100
# 
# general idea for primacity testing
# look for envidence that n is not a prime
# if find it, say n is composite, otherwise n is prime
# 
# trial division
# input: positive integer N, lg(N) = n // N represented with O(n) bits
# for i in 2...sqrt(n):
#   if i | N:
#       return yes
# return no
# 
# running time O(sqrt(n))
# 
# use randomized method
# main idea - use fermat's little theorem
# 1st try - contrapositive
# no need to factor
# but not so fast
# 
# 2nd try - converse
# converse is not always true
# possible when n is composite for some a, but gcd(a, N) = 1, to satisfy a^(N-1) = 1 mod N
# even more, psooible for all a, gcd(a, N) = 1, to satisfy a^(N-1) = 1 mod N
# these numbers are called carmichael numbers
# 
# to use converse - rabin-miller introduced simple randmozed primality test
# used in practice today
# if N <= 1 or N is even
#       return no
#  if n <= 3
#       return yes
# screen for carmichael numbers
# fermat's test(N)
# 
# fermat's test
# a = random(2, N-1)
# if gcd(a, N) != 1
#       return "is composite"
# else if a^(N-1) != 1 mod N
#       return "is not composite"
# else
#       return "probably primay"
# 
# running time
# random - o(1)
# computing gcd(a, N) is O(log(N))
# computing a^(N-1) is O((logN)^2)
# total running time O((logN)^2)
# 
# theorem - if N is composite and N is not Carmichael
# P(fermat's test output is correct) is at least 1/2
# 
# fermat's test with monte carlo
# a = random(2, N-1)
# if gcd(a, N) != 1
#       return "is composite"
# else if a^(N-1) != 1 mod N
#       return "is not composite"
# else
#       repeat fermat's test k times
#       return "probably primay with probability 1-1/2^k"
# 
# 
# 