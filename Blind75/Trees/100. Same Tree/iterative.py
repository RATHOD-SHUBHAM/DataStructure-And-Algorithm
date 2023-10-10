# Tc ans Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque([(p,q)])

        while queue:
            p, q = queue.popleft()
            
            if not self.check_similarity(p,q):
                return False
            
            if p and q:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        
        return True
    
    def check_similarity(self, p, q):
        # Both the nodes are not present
        if not p and not q:
            return True

        # only if one node is present
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        else:
            return True
