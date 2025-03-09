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