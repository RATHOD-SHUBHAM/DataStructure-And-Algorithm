'''
    1. Get all the parent of p and q.
    2. Get all the ancestor of p.
    3. Find parent of q in ancestor of p. 
        [This is becasue, one of the ancesotor of p will be ancestor of q]
'''

# Tc and Sc :O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {
            root : None
        }

        stack = [root]

        # 1. Get all the parent of p and q.
        while p not in parent or q not in parent:
            node = stack.pop(0)

            if node.left:
                # adding parent
                parent[node.left] = node
                stack.append(node.left)
            
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        

        # 2. Get all the ancestor of p.
        ancestor = set()
        while p:
            ancestor.add(p)
            # get ancestor of p
            p = parent[p]
        
        # 3. Find parent of q in ancestor of p.
        while q not in ancestor:
            q = parent[q]
        
        # found the common ancestor
        return q