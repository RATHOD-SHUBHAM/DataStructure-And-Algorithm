# --------------------  Vertical Order Traversal --------------------


# Tc and Sc: O(N)

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.level_wise_node = collections.defaultdict(list)
        self.max_row = 0

    def bfs(self, root):
        queue= [[root, 0]] # Node, Level

        while queue:
            node, level = queue.pop(0)

            self.level_wise_node[level].append(node.val)
            self.max_row = max(self.max_row, level)

            if node.left:
                queue.append([node.left, level + 1])
            
            if node.right:
                queue.append([node.right, level + 1])
        
        return 

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Step 1: BFS: Traverse the tree and store the nodes
        self.bfs(root)
        # print(self.level_wise_node)

        # Step 2: Extract the right side node
        op = []
        for row in range(0, self.max_row + 1):
            op.append(self.level_wise_node[row][-1])
        
        return op
        

# -------------------- Optimized Vertical Order Traversal --------------------

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.level_wise_node = collections.defaultdict(int)

    def bfs(self, root):
        queue= [[root, 0]] # Node, Level

        while queue:
            node, level = queue.pop(0)

            if level not in self.level_wise_node:
                self.level_wise_node[level] = node.val


            if node.right:
                queue.append([node.right, level + 1])
            
            if node.left:
                queue.append([node.left, level + 1])
            
        
        return 

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Step 1: BFS: Traverse the tree and store the nodes
        self.bfs(root)
        # print(self.level_wise_node)

        op = []
        for row, val in self.level_wise_node.items():
            op.append(val)

        return op
    

# -------------------- Queue Recursive --------------------

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If level == len(op):
    Then this node is being encounterd for the first time
'''
class Solution:
    def __init__(self):
        self.op = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level = 0
        self.dfs(root, level)

        return self.op
        
    def dfs(self, root, level):
        """Root >> Right >> Left"""
        if not root:
            return
        
        # Root
        if level == len(self.op):
            self.op.append(root.val)
            
        # Right
        self.dfs(root.right, level + 1)

        # Left
        self.dfs(root.left, level + 1)
        
        return
    


# -------------------- Queue Iterative --------------------

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If level == len(op):
    Then this node is being encounterd for the first time
'''
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        queue = [[root, 0]] # Node, level

        while queue:
            node, level = queue.pop(0)

            if level == len(op):
                op.append(node.val)
            
            # Go right and then go left
            if node.right:
                queue.append([node.right, level + 1])
            
            if node.left:
                queue.append([node.left, level + 1])
        
        return op