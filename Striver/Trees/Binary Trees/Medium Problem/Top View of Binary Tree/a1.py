# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import defaultdict
import math

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        op = []
        
        dic = defaultdict(list)
        
        queue = [[root, 0, 0]] # node, row, col
        
        min_col = math.inf
        max_col = -math.inf
        
        while queue:
            node, row, col = queue.pop(0)
            
            dic[col].append([row, node.data])
            min_col = min(min_col, col)
            max_col = max(max_col , col)
            
            if node.left:
                queue.append([node.left, row+1, col-1])
            
            if node.right:
                queue.append([node.right, row+1, col+1])
        
        
        
        for col in range(min_col, max_col + 1):
            lst = dic[col]
            op.append(lst[0][1])
        
        # print(op)
        return op
    
# --------------------------------- Modified ---------------------------------
from collections import defaultdict

# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.val = val
#         self.left = None

class Solution:
    def __init__(self):
        self.min_col = 0
        self.max_col = 0
        
        self.column_wise_data = defaultdict(int)
    
    # Vertical Order Traversal
    def bfs(self, root):
        queue =[[root, 0]] # Node, Column
        
        while queue:
            node, col = queue.pop(0)
            
            if col not in self.column_wise_data:
                self.column_wise_data[col] = node.val
            
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            
            if node.left:
                queue.append([node.left, col - 1])
            
            if node.right:
                queue.append([node.right, col + 1])
        
        return
            
        
    def topView(self,root):
        if not root:
            return []
        
        # Grab the value column wise
        self.bfs(root)
        # print(self.column_wise_data)
        
        op = []
        for col in range(self.min_col, self.max_col + 1):
            op.append(self.column_wise_data[col])
        
        return op