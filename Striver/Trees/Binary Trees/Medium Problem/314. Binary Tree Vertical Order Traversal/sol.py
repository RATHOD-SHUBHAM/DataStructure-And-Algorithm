from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.min_val = 0
        self.max_val = 0

        self.column_wise_data = defaultdict(list)
    
    def bfs(self, root):
        queue = [[root, 0 , 0]] # Node, Row, Col

        while queue:
            node, row, col = queue.pop(0)

            self.column_wise_data[col].append([row, node.val])
            self.min_val = min(self.min_val, col)
            self.max_val = max(self.max_val, col)

            if node.left:
                queue.append([node.left, row + 1, col - 1])
            
            if node.right:
                queue.append([node.right, row + 1, col + 1])
        
        return


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Step 1: Grab the data column wise
        self.bfs(root)

        # Step 2: Sort the value
        op = []

        for col in range(self.min_val, self.max_val + 1):
            temp = []
            for row, val in self.column_wise_data[col]:
                temp.append(val)
        
            op.append(temp)
        
        return op
        