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