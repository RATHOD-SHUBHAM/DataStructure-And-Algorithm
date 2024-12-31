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
            
        
        # Step 2: find the target -> here the target node is already given

        # Step 3: Mark the distance
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