"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        op = []
        
        stack = [root]

        while stack:
            node = stack[-1]

            if not node.children:
                node = stack.pop()
                op.append(node.val)
                continue
            
            for child in reversed(node.children):
                stack.append(child)
                   
            # Break the connection
            node.children = None

        return op
