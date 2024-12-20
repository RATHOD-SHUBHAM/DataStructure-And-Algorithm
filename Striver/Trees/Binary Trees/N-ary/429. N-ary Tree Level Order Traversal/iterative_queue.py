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

        queue = [[root, 0]]

        while queue:
            node, level = queue.pop(0)

            if len(op) == level:
                op.append([])
            
            op[level].append(node.val)

            for child in node.children:
                queue.append([child, level + 1])
            
        return op


        