# ----- Recursive Solution -----

from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def __init__(self):
        self.op = []
        
    def Paths(self, root):
        if not root:
            return []
        
        cur_path = []
        self.dfs(root, cur_path)
        
        return self.op
    
    def dfs(self, root, cur_path):
        cur_path = cur_path + [root.data]
        
        if not root.left and not root.right:
            self.op.append(cur_path)
            return 
    
        if root.left:
            self.dfs(root.left, cur_path)
        
        if root.right:
            self.dfs(root.right, cur_path)
        
        return
    
# -------- Iterative Solution --------

from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def __init__(self):
        self.op = []
        
    def Paths(self, root):
        if not root:
            return []
        
        path = [root.data]
        stack = [[root, path]]
        
        while stack:
            node, path = stack.pop()
            
            # if leaf node
            if not node.left and not node.right:
                self.op.append(path)
                continue
            
            if node.right:
                new_path = path + [node.right.data]
                stack.append([node.right, new_path])
            
            if node.left:
                new_path = path + [node.left.data]
                stack.append([node.left, new_path])
        
        return self.op