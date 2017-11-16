"""
Given a binary tree t, determine whether 
it is symmetric around its center, 
i.e. each side mirrors the other.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

"""

from tree import Tree

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
# 
# param t: tree
# return boolean
def isTreeSymmetric(t):
    
    if (t is None):
        return True
    
    # BFS queue
    queue = []
    values = []
    node = None
    
    # mark tree
    queue.append(t)
    n_node = 1 # number of node at cur depth
    
    while (len(queue) > 0):
        
        # get only node at cur depth
        while (n_node > 0):

            # pop queue
            node = queue.pop(0)

            # add new node
            if (node.left is not None):
                queue.append(node.left)
                values.append(node.left.value)
            else:
                values.append(None)
            
            if (node.right is not None):
                queue.append(node.right)
                values.append(node.right.value)
            else:
                values.append(None)

            # only get node at cur_depth
            n_node -= 1

        # check if mirror
        if (not isPalindrome(values)):
            return False
    
        n_node = len(queue)
        values = []
        
    return True
# 
# list_tree: list of integer
# return true if palindrom
# 
def isPalindrome(list_tree):
    return list_tree == list_tree[::-1]
    
    
def main():
    
    t = Tree(1)
    t.left = Tree(2)
    t.right = Tree(2)
    t.left.left = Tree(3)
    t.left.right = Tree(4)
    t.right.left = Tree(4)
    t.right.right = Tree(3)
    
    print(isTreeSymmetric(t))
    
    
main()