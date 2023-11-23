# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot) == True:
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        
        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)

        if leftTree == False or rightTree == False:
            return False
        else:
            return True