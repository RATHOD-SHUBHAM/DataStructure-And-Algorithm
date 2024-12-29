# Tc and Sc: O(n).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        stack_of_nodes = []

        for num in nums:
            node = TreeNode(num)

            # Set the smaller nodes as the left child
            while stack_of_nodes and stack_of_nodes[-1].val < num:
                node.left = stack_of_nodes.pop()
            
            # Set the current node as the right child
            if stack_of_nodes:
                # stack_of_nodes[-1] will be the max number
                stack_of_nodes[-1].right = node
            
            stack_of_nodes.append(node)
        
        # The root of the tree is the first node added to the stack
        return stack_of_nodes[0]