# NP-complete problems
# O(2^(n^k)) for some k > 0
# 
# intractable: a problem whose running time cannot be bounced by O(n^k) for any k > 0
# 
# classic np-complete problems
# 1. satisfiable = SAT
#       boolean formula in CNF (conjunctive normal form)
#       i.e. a conjunctino of clauses, each clause is a disconjunction or several literals
#       literals are either boolean variable or its negation
# a satisfying truth assignment (TVA) is an assignment of true or false to each variable
#       so that every clause contains a literal whose value is true
# SAT problem: given a boolean formula f(x_1...x_n) on  n variables in CNF, is there a TVA
#       to x_1...x_n that makes f(x_1...x_n) = true?
# in general, this kind of problem is solved using truth table
# the run time is O(m * 2^n)
# special case: 
#       horn SAT, each clause has at most one positive literal
#       2SAT, solved in O(m+n) time, each clause has 2 literals
# 
# in general, the time to verify a slotion is O(mn)
# 
# P and NP problems
# defition of P - the class of all problems that can be solved in polynomial time
# defintion of NP - the class of all problems if there exists a poly-time verifying algo
#       that takes an input as an problem instance I and a proposed solution S and outputs true
#       if and only if S is a solution to instance of I
# 
# 2. traveling salesman problem = TSP
#       given n vertices and graph is connected, and a budget b, is there a tour
#       meaning a cycle that passes through each vertex exactly once of cost  <= b
#       solve in general - exhaustive search, runs O((n-1)!) or DP O(n^2*2^n)
# 
# compare TSP vs MST
#   MST: given a weight matrix and a bound b, is there a spanning tree T
#       with total weight <= b
# 
#   diff - MST is looking for tree and TSP is looking for simple cycle
#       
# 3. hamilton cycle
#   hamilton cycle is a simple cycle that goes through every vertex exactly once
#   
# to prove a problem is NP-HARD, reduce an NP-HARD problem to new problem
# 
# 
# 1. SAT <= 3SAT
# x_1 <-> (x_1 v a v b)^(x_1 v a v not b)^(x_1 v not a v b)^(x_1 v not a v not a)
# if x_1 is true, right side must be true, because x_1 is in all clauses
# if x_1 is false, right side must be false, because some of all combinations of a,b must be true
# 
# (x_1 v x_2) <-> (x_1 v x_2 v c)^(x_1 v x_2 v not c)
# 
# 
# 
# 