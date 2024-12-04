# ----------------------------------- Recursive Approach -----------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        self.dfs(root, op)

        return op
    
    def dfs(self, root, op):
        # Left
        if root.left:
            self.dfs(root.left, op)
        
        # Root
        op.append(root.val)

        # Right
        if root.right:
            self.dfs(root.right, op)
        
        return
    
# ----------------------------------- Iterative Approach -----------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        stack = []

        node = root

        while node or len(stack) > 0:
            # Move left with help of node
            while node:
                stack.append(node)
                node = node.left
            
            # Left >> Root >> Right
            node = stack.pop() # pop out the left most node
            op.append(node.val)
            
            node = node.right # if this is root node, move right, else, move left using above while loop
        
        return op
