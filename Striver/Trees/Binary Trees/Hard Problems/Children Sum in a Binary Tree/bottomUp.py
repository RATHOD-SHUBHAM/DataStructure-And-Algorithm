'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        if not root:
            return 1
        
        return self.bottomUp(root)
        
    
    def bottomUp(self, root):
        if not root:
            return 1
            
        if not root.left and not root.right:
            return 1
            
        leftTree = self.bottomUp(root.left)
        rightTree = self.bottomUp(root.right)
        
        leftVal = 0 if not root.left else root.left.data
        rightVal = 0 if not root.right else root.right.data
        
        curTree = 1
        if root.data != leftVal + rightVal:
            curTree = 0
        
        return curTree and leftTree and rightTree