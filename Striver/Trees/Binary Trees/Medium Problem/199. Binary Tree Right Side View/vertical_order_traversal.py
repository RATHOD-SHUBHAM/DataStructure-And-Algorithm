# Tc and Sc: O(N)

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.level_wise_node = collections.defaultdict(list)
        self.max_row = 0

    def bfs(self, root):
        queue= [[root, 0]] # Node, Level

        while queue:
            node, level = queue.pop(0)

            self.level_wise_node[level].append(node.val)
            self.max_row = max(self.max_row, level)

            if node.left:
                queue.append([node.left, level + 1])
            
            if node.right:
                queue.append([node.right, level + 1])
        
        return 

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Step 1: BFS: Traverse the tree and store the nodes
        self.bfs(root)
        # print(self.level_wise_node)

        # Step 2: Extract the right side node
        op = []
        for row in range(0, self.max_row + 1):
            op.append(self.level_wise_node[row][-1])
        
        return op
        