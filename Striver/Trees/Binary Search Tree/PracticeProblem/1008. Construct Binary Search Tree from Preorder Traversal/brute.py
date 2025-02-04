# Brute Force: Insert Node into BST.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        # Create root node
        root = TreeNode(preorder[0])

        # Insert into BST
        for i in range(1, n):
            val = preorder[i]
            self.insertNode(root, val)
        
        return root
    
    def insertNode(self, root, val):
        if val < root.val:
            if root.left:
                self.insertNode(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                self.insertNode(root.right, val)
            else:
                root.right = TreeNode(val)

        