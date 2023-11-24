# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root

        queue = [root]

        op = []

        while queue:
            q_len = len(queue)

            for i in range(q_len):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                

                if i == 0:
                    op.append(node.val)
        
        # print(op)
        return op