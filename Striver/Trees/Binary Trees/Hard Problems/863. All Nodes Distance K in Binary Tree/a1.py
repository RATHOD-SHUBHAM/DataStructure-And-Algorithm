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
    

# ------------------------- BFS -------------------------

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

class Solution:
    def __init__(self):
        self.parents = {}

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Grab parents nodes
        queue = [root]
        self.parents[root] = None
        while queue:
            node = queue.pop(0)

            if node.left:
                self.parents[node.left] = node
                queue.append(node.left)
            
            if node.right:
                self.parents[node.right] = node
                queue.append(node.right)
            

        # Step 2: Mark the distance
        op = []
        visited = set()
        queue = [[target, 0]] # node, distance
        
        while queue:
            node, dist = queue.pop(0)

            if node.left:
                # Check if this nodes distance is already marked
                if node.left not in visited:
                    queue.append([node.left, dist + 1])
            
            if node.right:
                if node.right not in visited:
                    queue.append([node.right, dist + 1])
                

            if node in self.parents:
                # Check if it not a root node
                if self.parents[node] != None and self.parents[node] not in visited:
                     queue.append([self.parents[node], dist + 1])
            
            # Mark the current node as visited
            visited.add(node)

            if dist == k:
                op.append(node.val)
        
        return op