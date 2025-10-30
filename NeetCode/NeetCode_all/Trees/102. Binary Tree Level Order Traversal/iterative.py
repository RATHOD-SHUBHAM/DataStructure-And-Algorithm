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