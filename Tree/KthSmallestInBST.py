"""
Codefight

Note: Your solution should have only one BST traversal and O(1) extra space complexity, since this is what you will be asked to accomplish in an interview.

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and the right subtrees must also be binary search trees.

Given a binary search tree t, find the kth smallest element in it.
"""
import sys
from tree import Tree

# Morris Traversal
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(root, k):
    
    # count to iterate over elements
    count = 0
    
    # store ksmall
    ksmall = - sys.maxsize - 1
    cur = root
    
    while (cur is not None):
        
        if (cur.left is None):
            count += 1
            
            # if found ksmall
            if (count == k):
                ksmall = cur.value
            
            # go to parent right_child
            cur = cur.right
        
        else:
            # create link for Inorder 
            pre = cur.left
            while (pre.right is not None) and (pre.right != cur):
                pre = pre.right
                
            # building links
            if (pre.right is None):
                pre.right = cur
                cur = cur.left
            else:
                # revert changes
                pre.right = None
                count += 1
                if (count == k):
                    ksmall = cur.value
                    
                
                cur = cur.right
        
    return ksmall
        
        
def main():
    t = Tree(3)
    t.left = Tree(1)
    t.right = Tree(5)
    t.right.left = Tree(4)
    t.right.right = Tree(6)
    
    
    a = kthSmallestInBST(t, 5)
    print(a)
    
main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

