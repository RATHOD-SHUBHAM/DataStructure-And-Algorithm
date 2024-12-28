# This solution works because the number of nodes are limited.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Consider 0 index children
# Tc and Sc: O(n)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [[root, 0]] # Node, Position

        width_of_tree = -math.inf

        while queue:
            q_len = len(queue)

            left_most_node = queue[0][1] # left most child position

            for _ in range(q_len):
                node, i = queue.pop(0)

                if node.left:
                    left_child_position = 2 * i + 1
                    queue.append([node.left, left_child_position])
                
                if node.right:
                    right_child_position = 2 * i + 2
                    queue.append([node.right, right_child_position])
            
            # i will currently be holiding the position of right most node
            cur_width = i - left_most_node + 1
            width_of_tree = max(width_of_tree, cur_width)
        
        return width_of_tree