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