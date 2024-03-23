# flow network
# definition: a flow network is a directed graph G=(V,E)
#   with a source vertex s in V, 
#   a sink (target) vertex L in V
#   and one capacity
#   all edges have non-negative capacity
#   capacity definition v x v -> R, that assumes to each edge 
# defintion of flow:
#   a flow on G is a function f: V x V -> R satisfying constratints
#   capacity: 0 <= f(u,v) <= c(u,v)
#   conservation: for every vertex v in V, sum(f(u,v)) = sum((f(v, u)))
# definition 3
#   the value of a flow f is defined as the sum of flow out of source
# 
# max flow problem
# given a flow network G = (V,E,s,t,c) 
# 
# 
# residual capacity is defined as:
#   c_f(u,v) = 
#       c(u,v) - f(u,v) if (u,v) in E
#       f(u,v) if (v,u) in E
#       0 if (v,u) and (u,v) not in E
# 
# resudual grahp is a graph that contains same vertices V as G
#   with edges  E_f = {(u,v) in V x V: c_f(u,v) > 0}
# 
# an augmenting path P is a directed s -> t path from vertex s to vertex t in the residual graph G_f
# 
# 
# find a flow of max value
# edges in residual graph
# fowrad edge: for each edge in G for which f(u,v) < c(u,v)
# create an edge (u,v) in G_f and assign it capacity C_f(u,v) = c(u,v) - f(u,v)
# 
# backward edge: for each edge in G for which f(u,v) > 0
# create edge (v,u) in G_f
# and assign it a capacity of c_f(v,u) = f(u,v)
# 
# 
# ford-fulkerson algorithm
# for each edge (u,v) in G.E
# while (there exists on augmenting path P from s to tin the residual G_f)
#   find augmenting path P in G_f
#   compute capacity c_f(P) of P
#   // augment flow in G by c_f(P) along P
#   for each edge (u,v) in P
#       if(u,v) in G.E
#           f(u,v) = f(u,v) + c_f(p)
#       else
#           f(u,v) = f(u,v) - c_f(p)
# return f
# 
# claim if capacities are integers, then algorithm terminates
# proof:
#   |f'| > |f|, in fact, |f'| = |f| + c_f(p), mow c_f(p) is strictly positive
#   c_f(p) > 0, so always increasing the flow by some amount
#   there is only a finite capacity coming out of s, sum(c(s,v)) by capacity constraint
#   sum(f(s,v)) <= sum(c(s,v))
#   assumed capacities integers
# 
# a cut is a partition of vertices V into two subsets: S, V-S
# a s - t cut is a cut where s in S and t in V-S=T
# 
# capacity of a cut c(s,t)  = sum(c(u,v)), only edges cross the cut
# the flow across cut f(s,t) = sum(f(u,v)) - sum(f(v,u))
# 
# claim: f(s,t) <= c(s,t) by capcacity constraint
# theorem: for any flow network G, |f| = c(s,t) for some flow f and some cut(s,t)
# 
# theorem (max flow - min cut)
#   1. f is a max flow in G
#   2, G_f has no augmenting path
#   3. |f| = c(c,t) for some cut (s, t)
# 
# proof
#   (1) -> (2), if G_f has autmenting path P, then could add flow from s to get f+c_f(P)
#       so f was not a max flow
#  (2) -> (3) suppose G_f has no augmenting path, 
#       define cut s = {s} u {v: exists path for P from s to v in G_f with c_f(p) > 0}
#       T = V-S, cut(s,t)
#   claim: for each u in S and v in T, f(u,v) = c(u,v)
#       if (u,v) in E, f(u,v) = c(u,v), otherwise, c_f(u,v) = c(u,v) - f(u,v), (u,v) in E_f, v in S
#       if (v,u) in E, f(v,u) = 0, otherwise, c_f(u,v) = f(v,u) > 0, (u,v) in E_f, v in S
#       if (u,v) and (v,u) not in E, f(u,v) = 0 since c(u,v) = c(v,u) = 0
#   so f(s,t) = sum(f(u,v)) - sum(f(v,u))
#               = sum(c(u,v)) - 0 = c(s,t)
# 
# 
# analysis
#   O(E) per augmentation
#   if capacity is integer in [0,c], c is max capacity
#       then at most |F| <= c augmentations because each augmentation adds at least 1 to flow
#   if capacity is rational number, multiply least common mutliplier, then run as integer
#   so running time O(|E| * c)
#   
#   efficiency problem
#       there is no guidance on how to pick augmentation path
#       the algorithm can pick a path with small flow
#       to improve
#           1. BFS - shortest length augmenting path
#           2. Dijkastra - max capacity augmentation path
#       edmonds-karp uses BFS, run time becomes O(VE^2)
#       original ford-fulkerson takes O(|E| * c)
#       c can be log_2 C bits
#       so it's categorized as pseudo-polynomial time
# 
# application: bipartite matching
#   an undirected graph G=(V,E) is bipartite if V can be partitioned into 2 sets
#       L and R where V = L union R and for all e(u,v) in E, u in L and v in R
#   a matching M in an undirected graph G=(V,E) is a subset M of edges where no 2 edges
#       in M share a vertex, a matching M is maximum if for any matchings M' of G, |M'| <= |M|
# 
# reducce the problem to max flow problem
# create(G', s, t, c)
# for each vertex u in G.V
#   add u to G'.V
# add s, t to G'.V
# for each vertex u in L
#   add u to G'.adj[s]
#   c(s,u) = 1
# for each vertex v i R
#   add t to G'.adj[v]
#   c(v,t) = 1
# for each vertex u in L
#   for each vertex v in G.adj[u]
#       add v to G'.adj[u]
#       c(u,v) = 1
# for-fulkerson(G', s, t, c)
# return f
# 
# running time O(V+E) + O(|f|*|E|), |f| is the value off max flow f on G'
#   
#         
#   
#   
# 
# 






