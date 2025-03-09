# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curNode = root

        while curNode:
            if curNode.val == val:
                return curNode
            elif curNode.val < val:
                curNode = curNode.right
            else:
                curNode = curNode.left
        
        return None