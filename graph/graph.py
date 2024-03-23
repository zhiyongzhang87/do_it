# Graph G=(V,E)
# V = (Finite) set of vertices and V is not empty
# E  = set of edges, vertex paris (u, v), u, v in V
# if G is directed, then edge is ordered pair(u, v)
# if G is undirected, then edge is unorder pair(u, v)
# 
# undirected graph
# V = {a, b, c, d}
# E = {(a,b),(a,c),(b,c),(b,d),(c,d)}
# (u,v) = (v,u)
# 
# directed graph
# V = {a, b, c }
# E = {(a,c),(b,a),(b,c),(a,b)}
# (u,v) != (v,u)
# 
# loops (v,v) for v in V and multiple edges are typically excluded
# graph: two parameters describing size
# |V| = number of vertices
# |E| = number of edges (0 <= |E| <= |V^2|)
# running time is described in terms of both
# 
# graph representation
# adjacency list representation
# V = set of vertices, represented as array
# array of adj lists  |V| lined lists
# for each vertex n in V, adj[n] = list of vertices adj to n
# adj  list representation good for sparse graphs where |E| << |V^2|
# since space requirement is theta(V+E)
# 
# adj matrix representation
# assume V = {1,2...|V|}
# let A = (a_ij) = :
#       1 if (i,j) in E
#       0 if (i,j) not in E
# good for dense graph where |E| is close to |V^2|
# space require is theta(V^2)
# 
# 
# graph search
# given graph G, start vertex s in V
# assume directed, although need not be
# explore: visit every vertex reachable from s
# 1. s is reachable from s
# 2. if u is reachable from s, and v in Adj[u]
#   then v is reachable from s
# 3. only vertices reachable from s are those proved by 1 or 2
# 
# if u is reachable from s, then there is a path s->v_1->v_2->...->v_k->u
# (of length k+1) leading from s to u
# keep track of the paths:
# if v is discovered from u, then u is parent of v
# keep track of parent:
#   p[s] = nil, meaning no parent
#   p[v] = u, u is parent of v (u,v)
#   
# a path is simple if all of its vertices are distinct
# a circle is a closed path (v_0,v_1,...,v_k) with v_0 = v_k
# length of a path is the number of the edges
# the distance from u to v, is the length of shortest path
# from u to v
# a shortest path is not unique
# greedy algorithm
# what is closest(first) is the shortest
# breadth first search (BFS)
# input G=(V,E),  s in V, G adj list format
# output: BFS tree rooted at s
# start from sarting vertex s
# explore all vertices connected to s directly
# these are s children
# also record who has been added to the tree already
# so further explore doesn't add these vertices again
# since first and closest is the shortest
# 
# level of vertex in the tree corresponds to shortest distance to the root
# BFS tree is not unique
# invariant: distance
# 
# color of vertex:
#   white - not yet discovered
#   grey - discovered but not finished
#   black - finished (scanned adj list)
# 
# the algorithm keep track of 3 variables:
#   color[v] - status of v
#   d[v] - distance of v to s
#   p[v] - parent of v
# 
# maintain list of gray vertices in the order of discovery
# using FIFO queue
# only gray vertices are in the queue
# 
# BFS(G, S)
# for u in V
#   color[u] = white
#   d[u] = infty
#   p[u] = nil
# color[s] = grey
# d[s] = 0
# initialize Q as empty
# enqueue(Q, s)
# while Q is not empty
#   u = dequeue(Q)
#   for each v adjcent to u
#       color[v] = grey
#       d[v] = d[u] + 1
#       p[v] = u
#       enqueue(Q, v)
#   color[u] = black
# 
# 
# prove this algorithm
# to prove: d[v] is correctly computed for every v in V
# proof: assume some vertex v receives incorrect d[v] value
# clearly v != s, because d[v] = 0 only for v = s
# let u be the vertex immediately preceding v on shortest path
# from s to v, then e[s,u] = s[s,u]+1
# since d[u] is correctly set, d[u]=s[s,u] and s[s,v]=d[u]+1
# so d[v] > s[s,u] = d[u]+1
# since vertex u is dequeued from Q, v si either white, gray or black
# if white, then d[v] = d[u]+1 in code, contradicting
# if black, then v has already been removed from Q and d[v] < d[u], contradicting
# if gray, then v was colored gray on dequeuing since vertex w which was reached earlier from Q than u
# d[v] = d[w]+1, but then d[w] <= d[u] and d[v] = d[w]+1 <= d[u]+1, contradicting
# 
# each vertex added to QA at most once, so time complexity O(|V|)
# each adj list is examined at most once (of most 2|E|)
# running time O(V+E)
# 
# 
# 
# 
# DFS
# for each vertex u in V
#   color[u] = WHITE
#   p[u] = nil
# time = 0 // global variable
# for each vertex u in V
#   if color[u] == white
#       DFS-Visit(G, u)
# 
# DFS-Vist(G, u)
# time = time + 1
# d[u] = time
# color[u] = gray
# for each v in adj[u]
#   if color[v] == white
#       p[v] = u
#       DFS-Visit(G, v)
# color[u] = black
# time = time + 1
# f[n] = time
# 
# depth first search
# input G=(V,E), directed or undirected, in adj list format
# goal: explore every vertex and every edge
# output: d[v]: discovery time
#           f[v]: finishing time
#           p[v]: parent precessor of v on DFS tree
# run time theta(V+E)
#  
# tree edge (u,v) - vertex v white when edge(u,v) is explored 1st time
# d[u] < d[v] < f[v] < f[u]
# 
# back edge(u,v) - vertex v is gray when edge(u,v) is explored 1st time
# d[v] < d[u] < f[u] < f[v]
# 
# disconnected graph are split into different trees
# multiple runs of DFS-Visit
# each run corresponds to a connected component
# 
# outer loop goes through all vertices
# inner loop goes through all edges twice
# run time theta(V+E)
# 
# 
# for directed graph
# 4 types of edges
# tree edges
#   part of DFS tree, parent to child edge in DFS tree
#   (u,v), (gray, white)
# back edges
#   lead to ancestor in DFS tress
#   (u,v), (gray, gray)
# forward edges:
#   lead to nonchild descendants
#   (u,v), (gray, black)
# cross edgesL:
#   lead to neither anscestor nor descendant
#   (u,v), (gray, black)
# 
# the presence of back edge, then there's cycle in the graph
# for tree and forward edges (u,v)
# f[v] < f[u]
# for back edge (u,v)
# f[u] < f[v]
# 
# topological sort
# sort finish time backwards, high first, low last
# run time theta(V+E)
# regular sorting O(v lg v)
# 
# 
# 


