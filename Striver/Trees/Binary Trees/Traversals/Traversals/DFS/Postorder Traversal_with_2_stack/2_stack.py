# Using 2 stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack_1 = [root]
        stack_2 = []

        op = []

        # From a high level - this will create a ROOT > Right > Left kind of stack_2
        while stack_1:
            node = stack_1.pop()
            stack_2.append(node)

            if node.left:
                stack_1.append(node.left)
            
            if node.right:
                stack_1.append(node.right)
        
        # Get the values
        while stack_2:
            node = stack_2.pop()
            op.append(node.val)
        
        return op