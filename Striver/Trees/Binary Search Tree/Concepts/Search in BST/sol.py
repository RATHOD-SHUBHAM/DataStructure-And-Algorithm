# Tc and Sc: O(H) | O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.searchNode(root, val)

    def searchNode(self, root, val):
        if not root:
            return None
        
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchNode(root.left, val)
        else:
            return self.searchNode(root.right, val)
    
