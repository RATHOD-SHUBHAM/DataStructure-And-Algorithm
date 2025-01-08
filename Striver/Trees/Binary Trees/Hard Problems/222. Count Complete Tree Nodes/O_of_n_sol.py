'''
Total no of nodes in a binary tree at level l = 2 ^ l

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [[root , 0]] # Node, depth
        while queue:
            q_len = len(queue) # this will keep track of no of nodes at leaf level
            for _ in range(q_len):
                node, depth = queue.pop(0)

                if node.left:
                    queue.append([node.left, depth + 1])
                
                if node.right:
                    queue.append([node.right, depth + 1])
                
        depth -= 1 # grab the depth of before the leaf nodes
        return self.count_nodes(q_len, depth)

    def count_nodes(self, no_of_leaf_nodes, depth):
        """Count nodes at non leaf level"""
        total_nodes = 0
        total_nodes += no_of_leaf_nodes
        
        while depth >= 0:
            total_nodes += 2 ** depth # this will give the total no of nodes
            depth -= 1
        
        return total_nodes


# ----------- Easy Solution ----------------
# Tc and Sc: O(n) | O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.node_count = 0
        self.count = 0
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            self.count += 1
            self.node_count = max(self.node_count, self.count)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return self.node_count


# ----------- Easy Solution ----------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        op = []

        queue = [root]

        while queue:
            node = queue.pop(0)
            op.append(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return len(op)