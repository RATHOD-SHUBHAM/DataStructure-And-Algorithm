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
        
        stack = [root]

        while stack:
            node = stack.pop()
            op.append(node.val)

            for child in reversed(node.children):
                stack.append(child)
        
        return op