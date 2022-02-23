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
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # to keep a track of visited node
        # node will hold the clone of itself
        cache = {}
        
        def dfs(node):
            if not node:
                return
            
            if node in cache:
                return cache[node]
            
            # if not in cache: create a clone and add it in cache
            clone = Node(node.val,[])
            
            cache[node] = clone
            
            # dfs of child
            for nei in node.neighbors:
                clone.neighbors.append((dfs(nei))) # dfs will return the cloned node
            return clone
        
        return dfs(node)