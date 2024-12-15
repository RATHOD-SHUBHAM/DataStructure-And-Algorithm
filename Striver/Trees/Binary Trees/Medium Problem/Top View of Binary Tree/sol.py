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