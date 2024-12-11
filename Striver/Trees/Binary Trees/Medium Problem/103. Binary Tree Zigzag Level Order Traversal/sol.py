# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [[root, 0]]

        op = []

        while queue:
            _ , level = queue[0]

            temp = []

            q_len = len(queue)

            for _ in range(q_len):
                node, level = queue.pop(0)

                temp.append(node.val)

                if node.left:
                    queue.append([node.left , level + 1])
                
                if node.right:
                    queue.append([node.right , level + 1])
            
            # Reverse while saving the node in output
            if level % 2 == 0:
                op.append(temp)
            else:
                op.append(temp[::-1])
        
        return op
