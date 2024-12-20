"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:        
        op = []
        self.dfs(root, op)
        return op

    def dfs(self, root, op):
        if not root:
            return
    
        for child in root.children:
            self.dfs(child, op)
        
        op.append(root.val)

        return