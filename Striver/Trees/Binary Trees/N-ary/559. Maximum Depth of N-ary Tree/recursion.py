"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        return self.dfs(root)
        
    
    def dfs(self, node):
        if not node.children:
            return 1
        
        max_child_height = -math.inf
        for child in node.children:
            child_height = self.dfs(child)
            max_child_height = max(max_child_height, child_height)
        
        return 1 + max_child_height