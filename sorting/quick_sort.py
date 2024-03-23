# randomized algos
# what is a randomized algo?
# algo generate a random number r in [0...R]
# on same input on different executions
# a randomized algo may run a different number of steps
# or produce a different output
# in contrast to deterministic algos
# 
# randomized algos: in general 2 types
# monte carlo
#   always runs in same time
#   returns correct output with high probability
#   may be incorrect
# las vegas
#   always returns correct output
#   runs in expected time
#   not always the same time
# 
# las vegas: sorting
# ###########################################################
#   problem: sorting by comparison
#       insetion sort theta(n^2) in the case reversed sorted
#       merge sort o(nlgn) always
# ###########################################################
# new goal for sorting algo:
# find a sorting algo as fast as merge sort
# but sort in-place
# quick sort - divide and conquer
#   move the data while divide to achieve in-place sorting
# steps:
# 1. divide: partition input array into 2 sub-arrays around pivot x such that 
#       elements in left sub-array  <= x
#       elements in right sub-array > x
# 2. conquer: recursively sort sub-arrays using same quick sort
# 3. combine: nothing to do
# 
# pseudo code
# 
# quick_sort(A, p, r) // sort sub-array[p...r]
# if p < r                 // O(1)
#   q = partition(A, p, r) // theta(n)
# quick_sort(A, p, q-1)    // T(q-p): T(q-1)
# quick_sort(A, q+1, r)    // T(r-q): T(n-q)
# 
# partition(A, p, r)
# x = A[r]
# i = p-1
# for j = p to r-1
#   if A[j] <= x
#       i = i + 1
#       exchange(A[i], A[j])
# exchange(A[i+1], A[r])
# return i+1
# 
# time complexity
# T(n) = theta(n) + T(q-1) + T(n-q)
# 
# best case: if pivot always splits array into 2 equal size sub-arrays
# 
# worst case:
#   suppose input is A = [1...n]
#   1st pivot is n, left = [1...n-1], right is empty
#   2nd pivot is n-1
#   3rd pivot is n-2
#   ....
#   povit is 1
#   the total compares are 1+2+3+...+(n-1) = n(n-1)/2, theta(n^2)
#   
# what happens on most inputs?
# average run time is very close to best case
# distinguish between good and bad subarray splits
# call pivot x good if it uses within 25% and 75% of sorted array
# T(n) <= T(n/4) + T(3n/4) + O(n)
# T(n) = O(nlgn)
# in general, for 0 < a < b < 1, and a+b=1
# T(n) = T(an) + T(bn) + O(n)
# solves to T(n) = O(nlgn)
# 
# in reality
# data is not normally or uniformally distributed
# so we add randomness
# 1. pick a randomized pivot - randomized_parition(A, p, r)
#       ** pivot has to be chosen randomly in each recursive call
# i = random(p, r) // i is random from range [p...r]
#       random algo runs O(1)
# exchange(A[i], A[r])
# return partition as non-randomized partition
# 
# randomized_quick_sort(A, p, r)
# if p < r
#   q  = randomized_partition(A, p, r)
#   randomized_quick_sort(A, p, q-1)
#   randomzied_quick_sort(A, q+1, r)
# 
# analysis assume all array elements are distinct
# analyze expected running time
# compute upper bound on expected total number of comparisons
# lemma: for randomzied quick sort, expected number of comparison is <= 2n * ln(n)
# proof: input is A[1...n], let S[1...n] is sorted version of A
# for a pair S_i and S_j, they are compared at most once in the algo
# 1st time compared when either S_i or S_j is the pivot.
# then they are put in different sub-arrays
# so they won't be conpared again
# for i < j, let R_ij = 1 if S_i and S_j are compared, 
# or R_ij = 0 if they are not compared
# let R = total number of comparisons
#       = sum(i=1 to n-1 sum(j=i+1 to n R_ij))
# E(R) = E(sum(i=1 to n-1 sum(j=i+1 to n R_ij)))
#       = sum(i=1 to n-1 sum(j=i+1 to n E(R_ij)))
#  by linearity of expectation
# E(R_ij) = P(R_ij=1) + P(R_ij=0) = P(R_ij=1)
# consider S[1...n]
# if S_i or S_j is pivot chosen, then R_ij = 1
# P(R_ij = 1) = 2/(j-i+1) = E[R_ij]
# E[R] = sum(i=1 to n-1 sum(j=i+1 to n (2/(j-i+1))))
#       = 2 * sum(i=1 to n-1 (1/2 + 1/3 + ... + 1/(n-i+1))))
#       <= 2 * sum(i=1 to n-1 (1/2 + 1/3 + ... + 1/n)))
#       <= 2n(1/2 + 1/3 + ... + 1/n)
#       = 2nO(ln(n))
#       = O(nln(n))
# 
# improvement: cut of to heap sort then cut off to insertion sort
# median of three partitioning - CLRS problem 7-5, p.188
# 3-way partitioning - 7-2, p.186
# hoare partition - CLRS problem 7-1, p.187
# 

