"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        op = []

        stack = [[root, 0]]

        while stack:
            node, level = stack.pop()

            if len(op) == level:
                op.append([])
            
            op[level].append(node.val)

            for child in reversed(node.children):
                stack.append([child, level + 1])
            
        return op


        