# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent = {}
        self.ancestor = set()

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Get both p and q nodes parents and add to dictionary
        stack = [root]
        self.parent = {root : None} # there is no parent of root
        while p not in self.parent or q not in self.parent:
            """If any one of the nodes(p or q) is missing then keep looping"""
            node = stack.pop()

            if node.left:
                self.parent[node.left] = node
                stack.append(node.left)
            
            if node.right:
                self.parent[node.right] = node
                stack.append(node.right)
        
        # Get all the ancestors of one of the nodes
        while p:
            self.ancestor.add(p) # a node can be a descendant of itself according to the LCA definition.
            p = self.parent[p] # Keep moving upward

        # Check if there is a common ancestor
        while q not in self.ancestor:
            q = self.parent[q] # Keep moving upward
        
        # q is pointing to common ancestor
        return q

        



