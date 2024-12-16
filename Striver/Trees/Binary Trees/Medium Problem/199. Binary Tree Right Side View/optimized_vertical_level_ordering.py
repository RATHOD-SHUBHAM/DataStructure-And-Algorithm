# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.level_wise_node = collections.defaultdict(int)

    def bfs(self, root):
        queue= [[root, 0]] # Node, Level

        while queue:
            node, level = queue.pop(0)

            if level not in self.level_wise_node:
                self.level_wise_node[level] = node.val


            if node.right:
                queue.append([node.right, level + 1])
            
            if node.left:
                queue.append([node.left, level + 1])
            
        
        return 

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Step 1: BFS: Traverse the tree and store the nodes
        self.bfs(root)
        # print(self.level_wise_node)

        op = []
        for row, val in self.level_wise_node.items():
            op.append(val)

        return op