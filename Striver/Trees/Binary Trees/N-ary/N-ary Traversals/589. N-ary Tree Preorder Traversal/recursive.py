"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        op = []
        self.dfs(root, op)
        return op
    
    def dfs(self, root, op):
        if not root:
            return
        
        # Root, Children(LEFT, RIGHT)
        op.append(root.val)

        for child in root.children:
            self.dfs(child, op)
        
        return