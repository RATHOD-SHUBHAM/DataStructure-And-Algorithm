# ----------------------------- Inorder Traversal -----------------------------

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


# ----------------------------- PreOrder Traversal -----------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        op = []
        stack = [root]

        while stack:
            node = stack.pop()
            op.append(node.val)

            # Append in opposite direction
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
        
        return op



# ----------------------------- PostOrder Traversal -----------------------------

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

        while stack:
            node = stack[-1]

            # It can be a leaft node or root node. If this is the root node - then there will be no edges,
            if not node.left and not node.right:
                leaf_node = stack.pop()
                op.append(leaf_node.val)
            
            # Remove edges for the current node
            if node.right:
                stack.append(node.right)
                node.right = None
            
            if node.left:
                stack.append(node.left)
                node.left = None
        
        return op