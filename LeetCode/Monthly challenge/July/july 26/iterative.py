# Tc and Sc: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root : None}
        
        stack = [root]
        
        # get parents of p and q
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
                
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        # get ancestors of p and q
        
        ancestor = set()
        
        while p:
            ancestor.add(p)
            p = parent[p]
            
        while q not in ancestor:
            ancestor.add(q)
            q = parent[q]
            
        return q
            
        
        