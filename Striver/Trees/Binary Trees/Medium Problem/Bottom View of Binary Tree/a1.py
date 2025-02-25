class Solution:
    def __init__(self):
        self.min_col = 0
        self.max_col = 0
        
        self.column_wise_data = defaultdict(list)
    
    def bfs(self, root):
        queue =[[root, 0]] # Node, Column
        
        while queue:
            node, col = queue.pop(0)
            
            self.column_wise_data[col].append(node.data)
            
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            
            if node.left:
                queue.append([node.left, col - 1])
            
            if node.right:
                queue.append([node.right, col + 1])
        
        return
    
    def bottomView(self, root):
        if not root:
            return []
        
        # Grab the value column wise
        self.bfs(root)
        # print(self.column_wise_data)
        
        op = []
        for col in range(self.min_col, self.max_col + 1):
            op.append(self.column_wise_data[col][-1])
        
        return op
    

# --------------------------------- Modified ---------------------------------

from collections import defaultdict
import math
class Solution:
    def bottomView(self, root):
        op = []
        
        dic = defaultdict()
        
        queue = [[root, 0]] # node, col
        
        min_col = math.inf
        max_col = -math.inf
        
        while queue:
            node, col = queue.pop(0)
            
            # Replace the dic value each time. So, the last value will be stored in the dic
            dic[col] = node.data
            min_col = min(min_col, col)
            max_col = max(max_col , col)
            
            if node.left:
                queue.append([node.left, col-1])
            
            if node.right:
                queue.append([node.right, col+1])
        
        
        
        for col in range(min_col, max_col + 1):
            op.append(dic[col])
        
        # print(op)
        return op