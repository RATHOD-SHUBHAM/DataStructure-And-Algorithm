# Recursive -----------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        op= []
        level = 0

        self.bfs(root, op, level)

        return op

    def bfs(self, node, op, level):
        if not node:
            return
        
        if len(op) == level:
            op.append([])
        
        op[level].append(node.val)


        self.bfs(node.left, op, level + 1)
        self.bfs(node.right, op, level + 1)

        return op

# Iterative -----------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        op = []

        queue = [root]

        while queue:
            q_len = len(queue)

            ans = []

            for _ in range(q_len):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
                ans.append(node.val)

            op.append(ans)
        
        # print(op)
        return op