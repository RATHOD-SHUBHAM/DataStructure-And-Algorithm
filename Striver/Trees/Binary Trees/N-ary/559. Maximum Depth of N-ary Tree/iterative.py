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
        
        queue = [[root, 1]] # root, height

        max_height = 1

        while queue:
            node, cur_height = queue.pop(0)

            max_height = max(max_height, cur_height)

            if not node.children:
                continue
            else:
                for child in node.children:
                    queue.append([child, cur_height + 1])
        
        return max_height