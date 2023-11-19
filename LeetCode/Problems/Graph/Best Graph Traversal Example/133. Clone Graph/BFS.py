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

# bfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        # keep track of visited node and hold the clone of that particular node
        cache = {}
        
        cache[node] = Node(node.val,[])
        
        q = deque([node])
        
        while q:
            n = q.popleft()
            
            for nei in n.neighbors:
                if nei not in cache:
                    q.append(nei)
                    cache[nei] = Node(nei.val, [])
                
                # if nei in cache: that means they have already been visited and their clone is made. so just add them as neighbors of present clone
                cache[n].neighbors.append(cache[nei])
        
        return cache[node]