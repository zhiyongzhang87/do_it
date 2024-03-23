# Data structures:
# heaps, binary search tree, hashing
# linked list
# array - ordered, unordered
# 
# array unoredered array of key values
# insert/decrease-key O(1)
# exrtract-min: O(n)
# 
# binary heap
# an array visualized as a binary tree (nearly complete), can handle arbitray arrays
# 3, 10, 5, 11, 12, 6
#        3
#    10     5
#  11 12  6
# minimum height - O(lg n)
# requires:
#   each level is filled from left to right
#   and must be fillled before start next level
#   called left justified
# 
# head as a tree
# root: 1st element in the array A[i]
# parent(i) = floor(i/2)
# left(i) = 2i
# right(i) = 2i+1
# no pointer is needed
# 
# min-heap property (invariant)
# key[parent(i)] <= key[i] for all i > 1
# 
# 
# insert - place new key at bottom of the tree
# if smaller than parent, swap the two and repeat
# time complexity - O(lg n)
# 
# decrease-key (delete)
# bubble up and repair from it's current location
# 
# 
# extract-min: return root value O(1)
# place the right-most element at the bottom row at root
# repair by swap with smaller child and repeat if it's bigger than any of the child
# restore heap O(2lg(n)) = O(lg n)
# 
# to sort all elements
# can extract-min repeatedly from min-heap
# so time complexity of sorting is O(n lg(n))
# 
# 
# binary search tree
# maintain complete ordering of the data
# rooted binary tree
# each node x contains
# key[x] - data field
# three pointers
# left[x] points to left child
# right[x] points to right child
# p[x] points to parent
#   if root, p[x] is NULL
#   if child is missing, left[x] or right[x] is NULL
# 
# height of a tree
# the number of edges of longest simple downward path from root to leaf
# 
# traversal BST
# inorder tree walk
# if x != NULL
#   INORDERTREWALK(LEFT(X))
#   PRINT KEY[X]
#   INORDERTREEWALK(RIGHT(X))
# 
# initial call - INORDERTREEWALK(root[1])
# 
# tree search
# search(x, k) - x is a node, k is key to find
# if x == NULL or k == key[x]
#   return x
# if k < key[x]
#   return search(left[x], k)
# else
#   return search(right[x], k)
# 
# run time of search - O(H), worst O(n)
# 
# find min and max
# min = left most leaf
# max = right most leaf
# 
# min(x)
#   while left[x] != NULL
#       x = left[x]
#   return x
# 
# max(x)
#   while right[x] != NULL
#       x = right[x]
#   return x
# 
# run time for max and min - O(H)
# 
# 
# insert BST - property is maintained
# tree-insert(T, z)
#   y = NULL
#   x = root[T]
# while x != NULL
#   y = x
#   if key[z] < key[x]
#       x = left[x]
#   else
#       x = right[x]
# p[z] = y
# if y == NULL
#      root[T] = z
# else if key[z] < key[y]
#   left[y] = z
# else
#   right[y] = z
# 
# successor
#   successor of node x is the min of right sub-tree if x has right child
#   if x doesn't have right child, go up to parent repeated until root or x is the left sub-tree
# TreeSuccessor(x)
#   if right[x] != NULL
#       return tree-min(right[x])
#   y = p[x]
#   while y != NULL and x == right[x]
#       x = y
#       y = p[y]
#   return y
# 
# tree-delete
# 
# 
# 