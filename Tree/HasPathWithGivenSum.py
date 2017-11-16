import Tree 


#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, goal):
    
    if t is None:
        return (goal == 0)
    
    # get subSum
    ans = 0
    subSum = goal - t.value
    
    # if reach leaf, check
    if (subSum == 0 and t.left is None and t.right is None):
        return True
    
    # else, recursive tree
    if t.left is not None:
        ans = ans or hasPathWithGivenSum(t.left, subSum)
    if t.right is not None:
        ans = ans or hasPathWithGivenSum(t.right, subSum)
        
    return ans
   
   

    


def main():
    print("hello")
    
main()