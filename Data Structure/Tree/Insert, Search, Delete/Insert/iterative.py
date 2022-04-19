# Time = O(log N)
# Space = O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        
        while root:
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return head
                else:
                    root = root.left
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return head
                else:
                    root = root.right
                    
        return TreeNode(val)