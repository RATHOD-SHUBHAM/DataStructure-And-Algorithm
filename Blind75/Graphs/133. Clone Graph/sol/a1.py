# DFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_dict = {}

        return self.dfs(node, visited_dict)
    
    def dfs(self, node, visited_dict):
        if not node:
            return

        # check if the node has already been clone
        if node in visited_dict:
            return visited_dict[node]
        
        # Clone the current node
        cloned_node = Node(node.val , []) # node will have val and neighbors

        # add it to visited dict
        visited_dict[node] = cloned_node

        # clone the current nodes neighbors
        for nei in node.neighbors:
            cloned_node.neighbors.append(self.dfs(nei, visited_dict))
        
        return cloned_node

        

# ------------------------------------------------------------------------

# BFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        queue = []

        # get the first node, clone it and mark as visited
        visited_node = {}

        cloned_node = Node(node.val, [])
        visited_node[node] = cloned_node
        
        queue.append(node)

        while queue:
            cur_node = queue.pop(0)
            cur_cloned_node = visited_node[cur_node]

            # clone its neighbors
            for nei in cur_node.neighbors:
                # check if the nei is alrady clone
                if nei not in visited_node:
                    cloned_nei = Node(nei.val, [])
                    visited_node[nei] = cloned_nei
                    queue.append(nei)
                
                # add the nei to cloned node
                cloned_nei = visited_node[nei]
                cur_cloned_node.neighbors.append(cloned_nei)
            
        return cloned_node


