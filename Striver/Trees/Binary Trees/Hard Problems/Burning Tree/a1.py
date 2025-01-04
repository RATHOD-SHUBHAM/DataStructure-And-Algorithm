# ---------------- BFS ----------------

'''
Since we cant traverse in reverse direction, we cannot keep track of parent nodes.

3 Steps:
1. Keep track of parents.
2. Find the target node.
3. Grab the distance of the remaining nodes.
'''

import math

class Solution:
    def __init__(self):
        self.parents = {}
        self.max_time = -math.inf
        
    def minTime(self, root,target):
        # Step 1: Grab all node's parents
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

        
        # Step 2: Find the target node
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            if node.data == target:
                self.bfs(node)
                break
                
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
    
        return self.max_time
        
    
    def bfs(self, node):
        
        visited = set()
        
        queue = [[node, 0]] # node, dist
        
        while queue:
            node,dist = queue.pop(0)
            
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
            
            self.max_time = max(self.max_time , dist)



# ---------------- Adjacency List ----------------

'''
Since we cant traverse in reverse direction, we cannot keep track of parent nodes.

3 Steps:
1. Keep track of parents.
2. Find the target node.
3. Grab the distance of the remaining nodes.
'''

import math
from collections import defaultdict


class Solution:
    def __init__(self):
        self.adjaceny_list = defaultdict(list)
        self.max_time = -math.inf
    
    def build_adjacency_list(self, node, parent):
        cur_val = node.data
        if parent != None:
            self.adjaceny_list[cur_val].append(parent)
        
        if node.left:
            self.build_adjacency_list(node.left, node.data)
            self.adjaceny_list[cur_val].append(node.left.data)
        
        if node.right:
            self.build_adjacency_list(node.right, node.data)
            self.adjaceny_list[cur_val].append(node.right.data)
            
        
        
    def minTime(self, root,target):
        # Step 1: Grab all node's parents
        parent = None
        self.build_adjacency_list(root, parent)
        # print(self.adjaceny_list)

        self.bfs(target)
        return self.max_time
        
    
    def bfs(self, node):
        
        visited = set()
        
        queue = [[node, 0]] # node, dist
        
        while queue:
            node,dist = queue.pop(0)
            
            for nei in self.adjaceny_list[node]:
                if nei not in visited:
                    queue.append([nei, dist + 1])

            
            # Mark the current node as visited
            visited.add(node)
            
            self.max_time = max(self.max_time , dist)