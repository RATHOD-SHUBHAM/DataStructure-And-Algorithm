# ------------------ Recursive Solution -------------------

class Solution:
    def __init__(self):
        self.ceil = -1
        
    def findCeil(self,root, x):
        if not root:
            return self.ceil
        
        if root.key == x:
            self.ceil = root.key
            return self.ceil
        
        if x > root.key:
            return self.findCeil(root.right, x)
        else:
            self.ceil = root.key
            return self.findCeil(root.left, x)

# ------------------ Iterative Solution -------------------

class Solution:
    def findCeil(self,root, inp):
        # code here
        curNode = root
        ceil = -1
        
        while curNode:
            if curNode.key == inp:
                ceil = curNode.key
                break
            elif curNode.key < inp:
                curNode = curNode.right
                
            elif curNode.key > inp:
                ceil = curNode.key
                curNode = curNode.left
                    
        return ceil