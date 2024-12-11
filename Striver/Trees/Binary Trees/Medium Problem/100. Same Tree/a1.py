# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are not present
        if not p and not q:
            return True
        
        # if one of them is not present
        if not p or not q:
            return False
        
        # if the node value doesnot match
        if p.val != q.val:
            return False
        
        left_sub_tree = self.isSameTree(p.left, q.left)
        right_sub_tree = self.isSameTree(p.right, q.right)

        if left_sub_tree == True and right_sub_tree == True:
            return True
        else:
            return False


# ----------------------------------  Iterative  ----------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = [[p , q]]

        while queue:
            p , q = queue.pop(0)

            if not p and not q:
                continue
            
            # if one of them is not present
            if not p or not q:
                return False

            # if the node value doesnot match
            if p.val != q.val:
                return False
            
            queue.append([p.left, q.left])
            
            queue.append([p.right, q.right])
        
        return True
