# Fibonacci numbers
# F(n) // input non-negative integer
# if n = 0, return 0
# if n = 1 return 1
# return F(n-1)+F(n-2)
# 
# F(n) = phi^n = 1.618^n = 2^0.694n
# 
# T(n) = number of computer steps to compute F(n)
# T(n) <= 2 for n <= 1
# T(n) = T(n-1)+T(n-2)+3 for n > 1
# T(n) >= F(n), T(n) is exponential
# this algo is not efficient
# because a lot of steps are repeated to compute higher order results
# 
# F(n) improved
# if n = 0 return 0
# create an array f[0...n]
# f[0] = 0, f[1] = 1
# for i = 2 to n
#   f[i] = f[i-1] + f[i-2]
# return f[n]
# 
# dynamic programming
# good to solve problem with a lot of sub-problems with overlapping
# store the sub-problem results in a storage available to later steps
# the challenge is to find the relationship between sub-programs
# 
# 0/1 knapsack problem
# n items
# w[1...n] // weight of itmes
# v[1...n] // values of items
# weight limit
# 
# operation problem
# find subset S in [1...n] satisfying containts sum(w_i) <= W
# with objective of maximizing total value sum(v_i)
# 
# if we go through all the items each time, T(n) = 2^n
# 
# with integer weights
# this problem can be solved in O(nW) steps
# 
# use DP
# Idea: construct a table
#   each cell corresponds to a sub-problem with different input
#   x axis = weights
#   y axis = number of items
#   the cell value m[x,y] is the max value of items <= x with weight <= y
#   
# base cases:
#   when x = 0 or y = 0, [x,y] = 0
# 
# knapsack(n, w[1...n], v[1...n], W)
# for i = 0 to n
#   m[i,0] = 0
# for j = 1 to W:
#   m[0,j] = 9
# for i = 1 to n
#   for j = 1 to W:
#       if w_i > j
#           m[i, j] = m[i-1,j]
#       else m[i,j] = max{m[i-1,j], m[i-1, j-w_i]+v_i}
# return m[nW]
# 
# run time T(n) = O(nW)
# to retrieve the items in knapsack, compare current cell with the cell above it
# if m[x,y] != m[x,y-1], then itme y is included, then subtrack the weight
#   repeat with m[x,y-w_y]
# otherwise, analyze m[x,y-1]
# 
# 
# longest common subsequence
# given 2 sequences x[1...m], y[1...n]
# 
# define z[1...k] is a subsequence of x[1...m]
#   if there's a sequence of integers i[1...k], where i_x < i_y
#   such that z_j = x_i_j
# naive process
# check all subsequence in x if they are in y
# check all subsequence in y if they are in x
# 
# to improve, key idea:
# LCS of x and y can be expressed in terms of smaller subsequence
# if x_m = y_n, set last symbol of LCS to be this symbol
#   then recurse on x[1...m-1], y[1...n-1]
# if x_m != y_n, then LCS of x, y is either LCS of (x[1...m-1], y[1...n]) or (x[1...m], y[1...n-1])
# 
# the recursive tree height is O(m+n)
# run time is 2^O(m+n)
# exponential, not good
# now use DP
# create a table of length
# sub-problem is LCS-length(x[1...i], y[1...j])
# when x[i] == y[j], then LCS-length[i,j] = LCS-length[i-1,j-1] + 1
# othewise LCS-length[i,j] = max(LCS-length[i-1,j], LCS-length[i,j-1])
# base case: LCS-length[i,0] = 0, LCS-length[0,j] = 0
# 
# pseudo code
# create table c[0...m,0...n]
# for i = 1 to m
#   c[i,0] = 0
# for j = 0 to n
#   c[0,j] = 0
# for i = 1 to m
#   for j = 1 to n
#       if x[i] = y[j]
#           c[i,j] = 1 + c[i-1,j-1]
#       else
#           c[i,j] = max(c[i-1,j], c[i,j-1])
# 
# for DP alog, we need to create a table and store results
# for large inputs, this table can be big
# how to recover the results
# 
# strength of DP
# each sub-problem is only solved once
# drawback
# the solutions to some of the sub-problems may not be used
# 
# to improve - memorizing
# combine top-down (recursive) and bottom-up (DP) approaches
# sove only the sub-problems needed and solve only once (use trace)
# 
# pseudo code
# create table c[0...m,0...n]
# for i = 1 to m
#   c[i,0] = 0
# for j = 0 to n
#   c[0,j] = 0
# for i = 1 to m
#  for j = 1 to n
#       c[i,j] = 1
# return LookupLCS(m,n)
# 
# LookupLCS(m,n)
# if c[i,j] >= 0
#   return c[i,j]
# if x[i] == y[j]
#   c[i,j] = LookupLCS(i-1,j-1) + 1
# else
#   c[i,j] = max(LookupLCS(i-1,j), LookupLCS(i,j-1))
# return c[i,j]
# 
# 
# 


