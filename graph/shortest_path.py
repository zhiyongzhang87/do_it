# what is a shortest path
# shortest path from u to v
# is a path of minumum weight from u to v
# shortest path weight from u to v is delta(u,v) = min{w(p): p from u to v}
# 
# when do shortest path not exist?
# when there's a cycle p that w(p) is negative, delta(u,v) = -infty
# where there's no path from u to v, delta(u,v) = +infty
# 
# claim: a subpath of a shortest path is a shortest path
# proof:
# suppose p1 is a shortest path from u to v
# sub path p2 is from x to y and p2 is part of p1
# uppose p3 is the shortest path from x to y
# we should replace p2 with p3 which will make p1 shorter
# 
# Dijkstra's algorithm
# input: (G, w, s)
# G=(V, E), directed adjacency list format
# weight function w: E->R
# for all e in E, w(e) >= 0
# s in V, source vertex
# output: d[v] = distance = weight of a shortest(min-weight) path from s to v, for all v in V
# pi[v] = parent/predecessor of v on shortest paths tree
# 
# guarantee: the unique because the path from s to every vertex v in shortest paths tree is a shortest (min-weight) path
# d[v]: cuerrent min cost of reaching v
# 
# dijkstra(G, w, s)
# initialize-single-source(G, s)
# S = empty
# Q = V // keyed by d[v]
# while Q != empty
#   u = extract-min(Q)
#   S = S.append(u)
#   for each vertex v in Adj[u]
#       relax(u, v, w)
# 
# 
# initialize-single-source(G, s)
# for each vertex v in V
#   d[v] = infty
#   pi[v] = nil
# d[s] = 0
# 
# relax(u, v, w)
# if d[v] > d[u] + w[u,v]
#   d[v] = d[u] + w[u,v]
#   pi[v] = u
# 
# 
# proof
# d[v] = distance value assumed to vertex v by diskstra
# delta(s,v) = shortest path weight from s to v
# NTS: D[v] = delta(s,v) for all v 
# lemma: when u is deleted from Q, and added to S, d[u] = delta(s,u)
# inductive step: suppose u has just been deleted from Q
# IH: for all vertices B previously deleted from Q and added to S
# d[z] = delta(s,z), NTS: d[u] = delta(s,u)
# suppose not, d[u] != delta(s,u), know for any v when relax sets d[v] to a finite value
# there is always evidence of a path of that weight so d[v] >= delta(s,v) and so if d[u] != delta(s,u)
# then d[u] > delta(s,u), thus there is a shortest path from s to u with min weight < d[u] all this path P
# let y be the 1st vertex on P that is not in S(y might be u), and let x = pi[y]
# be predecessor of y on P then x = pi[y] in S, so by IH, d[x] = delta(s, x)
# since y was relaxed when x added to S
# so d[y] < d[u]
# contradiction
# so d[u] = delta(s,u), and algo correct
# 
# 
# reduction
# internet routing: delays on lines but also delays on routers
# what is the fastest (shortest aka min-cost) path from starting points through network?
# shortest paths: suppose in addition to edge weights {w(e): e in E}
# a directed graph has vertex costs: {c(v): v in V}
# define cost of path: sum of its edge weights + sum of costs of all vertices on path, including edning points of path
# 
# reduction
# all vertices have weight, so replace vertices with edge
# 
# modify dijkstra for negative weights
# 
# dijkstra(G, w, s)
# initialize-single-source(G, s)
# for each vertex v in V
#   d[v] = infty
#   pi[v] = nil
# d[s] = c(s)
# S = empty
# Q = V // keyed by d[v]
# while Q != empty
#   u = extract-min(Q)
#   S = S.append(u)
#   for each vertex v in Adj[u]
#       relax(u, v, w)
# 
# 
# initialize-single-source(G, s)
# for each vertex v in V
#   d[v] = infty
#   pi[v] = nil
# d[s] = 0
# 
# relax(u, v, w)
# if d[v] > d[u] + w[u,v] + c(v)
#   d[v] = d[u] + w[u,v] + c(v)
#   pi[v] = u
# 
# bellman-ford algorithm
# d[v]: current best estimate of shortest path weight from s to v
# idea: build trees of paths by relaxing all edges of graph (in arbitrary order)
#   then repeats until all edges relaxed |V| - 1 times
# 
# code:
# initialize-single-source(G, s)
# for i = 1 to |V| - 1 // |V|-1 is the longest simple path
#   for each edge(u,v) in E
#       relax(u, v, w)
# for each edge(u,v) in E
#   if d[v] > d[u] + w(u,v)
#       return False // negative weight cycle
#   else
#       return True // d[v] = delta(s,v)
#       
# as long as there's NO negative weight cycle, there's shortest path
# 
# proof:
# in absence of negative weight cycle
# d-values are 
# relax(u,v,w)
# d[v] = min{d[v], d[u] + w(u,v)} // DP elements
# it gives correct distance to v, when u is the 2nd to last vertex on the shortest paths to v and d[u] is correctly set
# it will never make d[v] too small
# if the graph is DAG, run topological sort, then just run one pass bellman-ford  
# 
# 
# 