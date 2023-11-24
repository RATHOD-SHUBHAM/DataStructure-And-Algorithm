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
            return node
        
        # Keep track of nodes
        queue = []
        queue.append(node)

        # Clone head
        dic = {}
        cloned_node = Node(node.val)
        dic[node] = cloned_node

        while queue:
            cur_node = queue.pop(0)
            cur_cloned_node = dic[cur_node]

            # Link neighbors
            for nei in cur_node.neighbors:
                # Clone neighbors
                if nei not in dic:
                    queue.append(nei)

                    cloned_nei = Node(nei.val)
                    dic[nei] = cloned_nei
                
                # Link the cloned nodes
                cloned_nei_node = dic[nei]
                cur_cloned_node.neighbors.append(cloned_nei_node)
        
        return dic[node]