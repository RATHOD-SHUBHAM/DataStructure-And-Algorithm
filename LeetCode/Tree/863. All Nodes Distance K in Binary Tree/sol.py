'''
Step 1: Get all the parents of each node
Step 2: Traverse in all the 3 direction(top, left, right) of upto k distance
'''
# Tc and Sc : O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = {}
        self.getParents(root, None) # root node will have none as its parent 
        return self.bfs(target, k)
    
    def getParents(self, node, parentNode):
        # base case
        if node is None:
            return
        
        # add parent node of current node in dic
        self.parent[node] = parentNode
        
        # call the subtree
        self.getParents(node.left, node)
        self.getParents(node.right, node)
        
        return
    
    def bfs(self, target, k):
        visited_node = set()
        queue = [(target, 0)] # k value is 0 initially
        result = []
        
        while queue:
            node , depth = queue.pop(0)
            
            # this node has been counted already
            if node in visited_node:
                continue
            
            # when depth matched k
            if depth == k:
                result.append(node.val)
                continue
                
            # add the current node to visited stack
            visited_node.add(node)
                
            # if i am at a node whose depth is not equal k, then i move in all 3 direction
            if node.left:
                queue.append((node.left ,depth + 1))
            
            if node.right:
                queue.append((node.right , depth + 1))
            
            if self.parent[node]:
                queue.append((self.parent[node] , depth + 1))
                
        return result