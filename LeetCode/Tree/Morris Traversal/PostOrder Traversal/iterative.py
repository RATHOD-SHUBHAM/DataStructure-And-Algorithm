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
        
        op = []
        stack = [root]
        
        
        while stack : 
            node = stack[-1] # last appended node
            
            # if this is a leaf node
            if not node.left and not node.right:
                op.append(stack.pop().val)
                
            # if there is right child
            if node.right:
                stack.append(node.right)
                node.right = None # break the node
            
            # if there is left child
            if node.left:
                stack.append(node.left)
                node.left = None # break the node
                
        return op