# ---------------- Longer Approach ----------------

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

import math

class Solution:
    #Function to find the minimum element in the given BST.
    def __init__(self):
        self.min_val = math.inf
        
    def minValue(self, root):
        ##Your code here
        if not root:
            return
        
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            self.min_val = min(node.data, self.min_val)
            
            if node.left:
                queue.append(node.left) 
        
        return self.min_val
    

# ---------------- Shorter Approach ----------------

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        if not root:
            return 0
        
        while root.left:
            root = root.left
        
        return root.data