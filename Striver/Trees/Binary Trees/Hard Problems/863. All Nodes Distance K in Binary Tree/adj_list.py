# Tc and Sc: O(n)

'''
Since we cant traverse in reverse direction, we cannot keep track of parent nodes.

3 Steps:
1. Keep track of parents.
2. Find the target node.
3. Grab the distance of the remaining nodes.
'''
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def __init__(self):
        self.neighbors = defaultdict(list)
    
    def build_adjList(self, node, parent):
        if parent != None:
            self.neighbors[node].append(parent)
        
        if node.left:
            self.neighbors[node].append(node.left)
            self.build_adjList(node.left, node)
        
        if node.right:
            self.neighbors[node].append(node.right)
            self.build_adjList(node.right, node)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Grab parents nodes
        parent = None
        self.build_adjList(root, parent)
            
        
        # Step 2: find the target -> here the target node is already given

        # Step 3: Mark the distance
        op = []
        visited = set()
        queue = [[target, 0]] # node, distance
        count = 0
        
        while count <= k:
            q_len = len(queue)
            count += 1

            for _ in range(q_len):
                node, dist = queue.pop(0)

                visited.add(node)

                if dist == k:
                    op.append(node.val)
                
                for nei in self.neighbors[node]:
                    if nei not in visited:
                        queue.append([nei, dist + 1])
            
        return op
    
# ----------------------- Iterative -----------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.neighbor = collections.defaultdict(list)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack = [[root, None]]

        while stack:
            node,parent = stack.pop()

            if parent != None:
                self.neighbor[node].append(parent)

            if node.left:
                self.neighbor[node].append(node.left)
                stack.append([node.left, node])
            
            if node.right:
                self.neighbor[node].append(node.right)
                stack.append([node.right, node])
        
        op = []
        visited = set()

        stack = [[target, 0]]

        count = 0 

        while count <= k:
            s_len = len(stack)

            for i in range(s_len):

                node, dist = stack.pop(0)
                visited.add(node)

                for nei in self.neighbor[node]:
                    if nei not in visited:
                        stack.append([nei, dist + 1])

                if dist == k:
                    op.append(node.val)

            count += 1
        
        # print(op)
        return op
        