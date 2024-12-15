# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.min_column = 0
        self.max_column = 0
        # Group the Nodes based on their Column or verticals
        self.column_wise_data = defaultdict(list) # Key = column , value = (row, node)
    
    def bfs(self, root):
        queue = [(root, 0, 0)] # Node, Row, Column

        while queue:
            node, row, column = queue.pop(0)

            self.column_wise_data[column].append((row, node.val))
            self.min_column = min(self.min_column, column)
            self.max_column = max(self.max_column, column)

            # left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1)
            if node.left:
                queue.append((node.left, row + 1, column - 1))
            
            if node.right:
                queue.append((node.right, row + 1, column + 1))
        
        return

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # step 1). BFS traversal
        self.bfs(root)
        # print(columnTable)

        # step 2). Extract the values from the columnTable
        op = []
        for col in range(self.min_column, self.max_column + 1):
            # sort first by 'row', if they belong to same row then sort by 'value', in ascending order
            temp = []
            for row, val in sorted(self.column_wise_data[col]):
                temp.append(val)
            op.append(temp)

        return op