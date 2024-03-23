# minimum spanning trees
# input: connected, undirected, graph G=(V,E)
#       with weight function: w: E -> r
# OUTPUT: A SPANNING TREE T=(V,E'), E' in E
# connects all vertices of minimum weights
# 
# w(T) = sum(w(u,v))
# 
# sort edges with weights
# start from least weighted edge
# try to include it in the spanning tree
# if both ends are already connected to the spanning tree
# then skip this edge
# 
# this is greedy algorithm
# greedy choice property: local optimal
# choices lead to globally optiomal solutions
# 
# kraskal's algorithm
# 1. sort the edges by weight
# 2. choose any edge with smallest weight (edges can have same weight)
#       put it in MST constructing
# 3. successively consider remaining edges in the order of increasing weight
#       try to add them to MST if it does not create a cycle 
#       with edges already in MST
# 
# Kraskal(G, M) // M = |E|, |V| = # of vertices
# sort edges by weight
# X = empty // edges in MST
# for i in 1...M:
#   if E[i] does not create a cycle with edges in X
#       then add E[i] to X
#   
# run time analysis
# sort edges takes O(E lg E)
# E <= V^2, lg E <= lg V^2 = 2 lg V  
# loop runs O(V)
# naive solution: DFS * O(V) to find a cycle
# time: O(E lg V) + O(VE) + O(V) = O(VE)
# 
# cut property
# definition: A cut in a graph G=(V,E) is any partition of verices V into two subset S and V - S
# theorem: for any cut(S, V-S) in a connected undirected graph G(V,E,w)
#   any least weight edge e=(u,v) crossing the cut, i.e. u in S, v in V-S, is in some MST of G
# proof: 
#   let T be an MST of G, if T contains e=(u,v), then proved
#   if e is not in T
#       since T is a tree, there is a unique path between any two vertices in T
#       since T is spanning tree, T contains all vertices, there is a unique path in T between u and v
#       since u is in S and v is in V-S, the path from u to v must contain some edge e'=(x,y) crossing the cut(S,V-S)
#           x is in S, and y is in V-S
#       if add e=(u,v) to T, e' and e form a cycle T U {e}
#       if remove e' from T, then get T-e' U {e}
#       then T'=T-(x,y) + (u,v) is a spanning tree
#   T' must have the same weight as T
#   since (u,v) is the least weight edge crossing (S,V-S), so w(u,v) <= w(x,y)
#   if w(x,y) > w(u,v), then w(T') < w(T)
#   but T is MST, so w(T') = w(T)
# 
# cycle property
# let G=(V,E) be a connected undirected weighted graph
# let e=(u,v) be a minimum weighted edge on some cycle C of G
# then there is an MST of G that does not containing e
# proof:
#   suppose e beongs to T
#   removing e from T disconnects T into 2 subtrees of G 
#       (as a tree, there's a unique path between any 2 vertices, so removing an edge disconnects a tree)
#   consider the cut(S,V-S) formed by 2 subtrees when e is removed
#   let S be one side of the cut
#   since e=(u,v) is on a cycle, there is a path from u to v on C
# some other edges on C, say e', has exactly one end point in S
# since e is a max-weight edge on C, w(e') <= e(e)
# replace e with e' will give another spanning tree with weight no greater than original MST
# 
# prim's algorithm: what is the relevant cut?
#   let s be the subset of vertices in current tree T
#   add cheapest edge e with exactly one endpoint in S
#   cut property asserts that e is in an MST
# question: how to find cheapest edge with exactly one endpoint in S?
# answer: use min-priority queue
# 
# prim(G, w, r) // G(V, E) adj list format, r is in V
#   maintian 2 hashtables
#       key[u] = weight of an edge connecting u to a vertex in S
#       pi[u] = parent of u
#       mark[u] = 0 if u is in Q
# 
# for each u in V
#   key[u] = infy
#   pi[u] = nil
#   mark[u] = 0
# 
# key[r] = 0
# mark[r] = 1
# Q = V // ordered by key[u]
# while Q is not empty:
#   u = extract-min(Q)
#   mark[u] = 1
#   for each v in adj[u]:
#       if mark[v] == 0 and w(u,r) < key[u]
#           key[v] = w(u,v)
#           pi[v] = u
# 
# almost identity to Dijskstra
# difference:
#   in prim, key[v] = weight of an edge connecting v to a vertex in S
#   in Dijkstra, d[v] = current min weight of an entire path from s to v
# 
# time complexity
# |V| * cost of insert + |V| * cost of extract min + O(E) * cost of decreasing-key
# 
# 1. array O(V^2)
# 2. binary min-heap: O((V+E) lg V) = O(E lg V) because G is connected
# spanning tree |E| = |V| - 1
# 
# 
# krushal: what is the relevant cut?
# 1. edges sorted in order
# 2. if adding e=(u,v) to T does not create a cycle
# 3. then e is the min-weight edge with exactly 1 endpoint in S
# 4. so cut property asserts that e is in some MST
# 
# to handle #2, how to check if adding an edge to T would create a cycle?
# use union-find data structure
# maintains a set for each connected component
# if u,v in same connected component, then adding (u,v) creates cycle, don't!
# if not, add(u,v) to T, merge = union sets containing u and v
# 
# initially each vertex is a connected component (CC) by itself
# makeset(u)
# algorithm test pairs of vertices to determine if belong to same CC
# find(u)
# when add edge, join 2 CCs, union(u,v) merges sets containing u and v
# 
# krushal(G, w)
# x = empty set // edges in MST
# for v in V
#   makeset(v)
# sort(E)
# for each edge(u,v) in E // in increasing order of weight
#   if find(u) != find(v)
#       x.add((u,v))
#       union(u,v) // merge 2 CCs
# 
# makeset(u)
#   pi(u) = u
#   rank(u) = 0 // height of subtree hanging from u
#   
# find(u)
#   while u != pi(u)
#       u = pi(u)
#   return u
# 
# union(u,v)
#   link(find(u), find(v))
# 
# link(x,y)
#   if rank(x) > rank(y)
#       pi(y) = x
#   else
#       pi(x) = y
#   if rank(x) == rank(y)
#       rank(y) = rank(y) + 1
# 
# by doing above, the height of the tree will be O(lg n)
#   
# time complexity 
# kruskal
# |V| makeset: O(1)
# 2|E| find: O(lg V)
# |V| - 1 union: O(1) if store results from find
# cost of initial sorting: O(E lg V)
# 
# overall cost
# O(V) + O(E lg V) + O(V) + O(E lg V)
# = O(E lg V)
# 
# to prove find runs O(lg n)
# claim: max height <= lg n, n = |V|
# property: a root of rank k has >= 2^k nodes in it's tree
# base case
#   k=0, 2^0 = 1
# inductive hypothesis
#   assume this is true for all m <= k
# induction
#   take root r of rank of k+1
#   r must have rank of k
#   and union with another vertex with rank of k
#   so by IH, root r of rank k has >= 2^k in the subtree
#   and so does vertex v
#   after union, r has >= 2 * 2^k = 2^(k+1) nodes in the tree
#   there are <= n/2^k vertices of rank k, where n = total num of vertices
#   max rank is log n, why?
#   suppose max rank is log n+1
#   <= n/2^k = n/2^(log(n+1)) = n/(2n) = 1/2 < 1
#   there can not be half vertex
# 