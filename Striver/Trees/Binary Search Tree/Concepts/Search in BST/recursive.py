# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)
    
    def search(self, root, k):
        if not root:
            return None
        
        if root.val == k:
            return root
        elif k < root.val:
            return self.search(root.left, k)
        else:
            return self.search(root.right, k)