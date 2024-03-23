# array A[1...n] is n distinct sorted numbers
# circularly shifted K positions to the right
# 
# goal: use O(lg(n)) to find the largest number in A
# divide the array, compare the mid with begin and end
# if mid < begin, then max is in A[begin...mid]
# if mid > end, then max is in A[mid...end]
# 
# proof
# base case: when array has 1 element, max is obvious
#            for array has 2 elements, max can be found by comparing them
# IH: algo finds max of array with size up to n
# induction: so when break array of size n+1 into 2 sub-arrays
#   the same algo will correctly find max of sub-arrays by IH
# 
# 
# 
# given a sorted arry a containing  n-1 distinc integers
# between 1 and n, give divide and conquer O(log(n)) algo
# to find the missing integer
# 
# find_missing(A[p...r])
# when 1st number is not p, then missing p
# when last number is not r, then missing r
# else
#   divide the array into 2 sub-arrays with mid=q
#   if A[q] - A[1] != q - 1
#       look into A[r...q]
#   else
#       look into A[q+1...r]
# 