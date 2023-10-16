'''
Nice graph traversal to understand BFS and DFS
https://www.youtube.com/watch?v=mQeF6bN8hMk

Time = O(N+M) , where N is no of node and M is no of edges
Space = O(N)

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# dfs

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

        