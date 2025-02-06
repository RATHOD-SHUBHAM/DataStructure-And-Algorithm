# ----------------------- Inorder Traversal -----------------------

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

# ----------------------- Inorder Traversal without search -----------------------

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
        
# ----------------------- Using BST property -----------------------

# Using BST property

# Tc: O(n) | Sc: O(1)

'''
Inorder property: Left , root , right

When we write inorder in BST we get a sorted array

If my p >= root:
    then successor wont be on left side, it will be on right side

But if p < root:
    Then this root can be a potential succesor, left -> root
    Then move left
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        node = root
        successor = None

        while node:
            if p.val >= node.val:
                # Move right: This node cant be a successor nor anybody on the left
                node = node.right
            else:
                # This node can be a potential successor
                successor = node
                node = node.left
        
        return successor
        