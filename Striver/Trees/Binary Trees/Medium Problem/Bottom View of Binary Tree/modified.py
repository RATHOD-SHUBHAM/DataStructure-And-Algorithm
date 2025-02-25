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