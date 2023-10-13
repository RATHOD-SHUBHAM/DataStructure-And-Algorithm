# Tc and Sc: O(n)

# This solution failt to analyse depth nodes
# eg: [5,4,6,null,null,3,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root)
    
    def isBST(self, root):
        if not root.left and not root.right:
            return True
        
        leftSubTree = True
        rightSubTree = True
        
        if root.left:
            leftSubTree = self.isBST(root.left)
        
        if root.right:
            rightSubTree = self.isBST(root.right)

        Valid_subTree = leftSubTree and rightSubTree
        
        leftNode = True
        rightNode = True
        
        if root.left:
            if root.left.val >= root.val:
                leftNode = False
        
        if root.right:
            if root.val >= root.right.val:
                rightNode = False
        
        return Valid_subTree and leftNode and rightNode


# ------------------------------------------------------------------------

# ===========

# Binary Tree property, with default function

# ===========

# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = -math.inf
        high = math.inf

        return self.isValid(root, low, high)

    # Assigning default value to function
    def isValid(self, root, low = -math.inf, high = math.inf) -> bool :
        if not root:
            return True
        

        # by assigning default value we take care of leaf nodes
        if (root.val <= low) or (root.val >= high):
            return False

        '''
            Left node val < root val
            right node val > root val

            so for left node -> higher val will be root
            and similary for right node -> lower val will be root
        '''
        
        return (self.isValid(root.left, low, root.val)) and (self.isValid(root.right, root.val, high))
    

# ------------------------------------------------------------------------

# Tc and Sc :O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        low = -math.inf
        high = math.inf

        stack = [(root, low, high)]

        while stack:
            node, low, high = stack.pop(0)
            
            if node.val <= low or node.val >= high:
                return False

            if node.left:
                stack.append((node.left, low , node.val))
            
            if node.right:
                stack.append((node.right, node.val, high))
        
        return True

            