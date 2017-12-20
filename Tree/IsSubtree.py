"""
Given two binary trees t1 and t2, 
determine whether the second tree is a subtree of the first tree. 
A subtree for vertex v in a binary tree t is a tree 
consisting of v and all its descendants in t. 
Determine whether or not there is a vertex v (possibly none) 
in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2

      t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1

As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).
"""

#
# Check if t2 is subtree of t1
# 
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     
def isSubtree(t1, t2):
    
    if t2 is None:
        return True
    
    if t1 is None:
        return False
    
    if areIdentical(t1, t2):
        return True
    
    # try left and right subtree
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)

    
def areIdentical(root1, root2):
    
    # Base Case
    if (root1 is None) and (root2 is None):
        return True
    if (root1 is None) or (root2 is None):
        return False
    
    # recursion
    return (root1.value == root2.value and areIdentical(root1.left,root2.left) and areIdentical(root1.right,root2.right))
