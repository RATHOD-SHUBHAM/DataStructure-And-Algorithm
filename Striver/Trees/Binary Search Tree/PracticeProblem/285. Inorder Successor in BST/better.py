# ------------------------ Recursive Solution ------------------------

# Brute Force: Inorder Traversal without search.
# Tc: O(n) | Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.successor = None
        self.found_p = False
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.inorderTraversal(root, p)
        return None if self.successor == False else self.successor
    
    def inorderTraversal(self, root, p):
        if not root:
            return
        
        leftTree = self.inorderTraversal(root.left, p)

        if self.found_p == True:
            # If this is my first occurance
            if self.successor == None:
                self.successor = root

        if root.val == p.val:
            self.found_p = True
        
        rightTree = self.inorderTraversal(root.right, p)


# ------------------------ Iterative Solution ------------------------

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
        
        
        