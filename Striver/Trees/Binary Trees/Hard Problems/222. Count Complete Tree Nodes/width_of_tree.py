# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_nodes = 0
        queue = [[root, 0]]

        while queue:
            q_len = len(queue)
            left_pos = queue[0][1]

            for _ in range(q_len):
                node, pos = queue.pop(0)

                new_pos = pos - left_pos

                if node.left:
                    left_child_pos = 2 * new_pos + 1
                    queue.append([node.left, left_child_pos])
                
                if node.right:
                    right_child_pos = 2 * new_pos + 2
                    queue.append([node.right, right_child_pos])
            
            cur_width = pos - left_pos + 1

            total_nodes += cur_width
        
        return total_nodes