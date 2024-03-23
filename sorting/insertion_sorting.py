

# start with 2nd element in the array
# compare the element e with all the elements x before it
# starts with e and x right before e
# if e < x, move x to the next position
# if e >= x, insert e after x and stop
# so the array is sorted from the beginning to to the position of e
def insertion_sort(values: list) -> list:
    pass


# prove correctness
# LI: at the start of each iteration of FOR loop(L1-I)
# keys originally in A[1...j-1] are in A[1...j-1] but in sorted order
# BASIS
# INITIALIZATION: LI is true initially j=2
# 
# INDUCTION STEP
# MAINTENANCE: IF LI is true before an iteration, it remains true after
# to insert jth item
# insert jth item after kth position
# because A[k] and A[j] are compared, so A[k]<=A[j]
# because A[k] and A[k+1] are sorted before this interation
# so A[j] < A[k+1]
# therefore, the sorted order is maintained
# 
# TERMINATION: LI is true when loop terminates j=n+1
# 
# Analysis
# T(n) = running time of algorithm on input of size n
# many inputs of given size
#   the value of the inputs doesn't matter
#   the order of the inputs matters
#   example of inputs: already sorted, reversely sorted, etc..
# T(n) = worse-case running time on an input of size n
#       = max(inputs x of size n) (running time on x)
# 
# basic operation of insertion sort: key comparision A[i] > key
# worst case: A[i] > key is executed the greatest number of times for every i
# since key  = a[j] and A[i] > A[j] for every i
# the worst case is reversely sorted array
# T(n) = sum((j-1) for j from 2 to n) = n(n-1)/2-n-1 -> quadratic
# best case: A[i] > key is executed only once for every i
# T(n) = sum(1 for j from 2 to n) = n-1 -> linear
# this is when array is already sorted
# 
# asymptotic analysis
# T(n) = 4n^2 + 22n + 12
# we don't care about constants, constant factors
# we only care about highest orders
# in this case, it's n^2
# BIG O - upper bound, def T(n)=O(g(n)) if exists n0 and c > 0
# such that 0 <= T(n) <= c*g(n) for all n >= n0
# 
# BIG OMEGA - lower bound
# T(n) = omega(g(n))
# def T(n) is omega(g(n)) if exists n0 and c >= 0
# such that 0 <= c*g(n) <= T(n) for all n >= n0
# in this case it's omega(n^2)
# 
# BIG THETA - if and only if T(n) = O(g(n)) and T(n) = omega(g(n))