# Brute Force: Inorder Traversal.
# Tc and Sc: O(n)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            inorder.append(node)

            root = node.right
        
        

        n = len(inorder)

        for i in range(n):
            curNode = inorder[i]

            if curNode == p:
                return inorder[i+1] if i + 1 < n else None
        
        return None