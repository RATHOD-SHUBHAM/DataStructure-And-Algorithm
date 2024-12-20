# -------------------------- Recursive  with Extra Space --------------------------

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
        
        max_child_height = []
        for child in node.children:
            child_height = self.dfs(child)
            max_child_height.append(child_height)
        
        return 1 + max(max_child_height)
    


# -------------------------- Recursive  --------------------------

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
    

# -------------------------- Iterative  --------------------------

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