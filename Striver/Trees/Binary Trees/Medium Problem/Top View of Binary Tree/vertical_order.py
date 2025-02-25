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