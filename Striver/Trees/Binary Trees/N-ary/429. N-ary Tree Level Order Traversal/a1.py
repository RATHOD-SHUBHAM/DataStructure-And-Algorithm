# -------------------------- Recursive --------------------------

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
        level = 0

        self.bfs(root, op, level)

        return op

    def bfs(self, root, op, level):
        if not root:
            return
        
        if len(op) == level:
            op.append([])
        
        op[level].append(root.val)

        for child in root.children:
            self.bfs(child, op, level + 1)
        
        return
    

# -------------------------- Iterative Stack --------------------------


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


# -------------------------- Iterative Queue --------------------------


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


        