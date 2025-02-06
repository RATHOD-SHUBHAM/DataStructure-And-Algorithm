# Brute Force: Inorder Traversal without search.
# Tc: O(n) | Sc: O(n)

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        found_p = False

        # Inorder Traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            
            if found_p == True:
                return node
            
            if node == p:
                found_p = True

            root = node.right
        
        return None
        
        
        