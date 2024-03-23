# merge sort
#  divide/conquer/combine paradigm
# input array of size n
# divide array into 2 arrays of size n/2
# sort each sub array separately
# divide recursively
# combine - merge sorted arrays
# 
# divide the array recursively until all subarrays has just one element
# [5 2 7 4 3 1 2 6]
# [5 2 7 4] [3 1 2 6]
# [5 2] [7 4] [3 1] [2 6]
# [5] [2] [7] [4] [3] [1] [2] [6]
# [2 5] [4 7] [1 3] [2 6]
# two finger method, use 1 point for each array to merge
# the smaller element is put into results and the pointer is moved to next
# [2 4 5 7] [1 2 3 6]
# [1 2 2 3 4 5 6 7]
# 
# merge 2 sorted subarrays
# copy 2 subarrays into temp storage
# then use 2 finger method to put all elements back to original array
# running time:
#   comparison A[j] < B[j]
#   each comparison decides the position of one element
#   running time is theta(n)
# use extra storage of n
# 
# correctness
# initialization
#   main loop is merge
#   before main loop, subarrays have to be sorted
# LI: at the start of each loop, compare the head of L and R array
#   put the smaller element into original array
# Termination: when point of L reaches the end of the array
# since subarrays are soreted before merge, the merged array is also sorted
# 
# BIG O
# solve recurrence
# interation method
#   CLRS chapter 4.4
# substitution method
#   guess solution
#   verify by induction
#   solve for constants
#   CLRS chapter 4.3
# master theorem
#   IF T(n) = aT(n/b) + O(n^d)
#   a >= 1, b > 1, d >= 0
#   when d > log_b^a, T(n) = O(n^d)
#   when d = log_b^a, T(n) = O(n^d * log(n))
#   when d < log_b^a, T(n) = O(n^(log_b^a))
#   proof - disguta p 49
# so merge sort O(nlg(n)), faster than insertion sort
# 
# MergeSort(A, p, r)
# if p = r
#   return
# else
#   q = floor((p+r)/2)
#   MergeSort(A, p, q)
#   MergeSort(A, q+1, r)
#   Merge(A, p, q, r)
# 
# Prove merge takes 2 sorted sub-arrays 
# use induction on size of sub-array
# base case: array with 1 element is sorted
# IH: 
# 
# 
# 