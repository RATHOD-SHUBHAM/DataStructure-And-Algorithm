# Tc and Sc: O(n) | O(h)


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
    

# ----------- Height of the tree ----------------

# Tc: O(logN) | Sc: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.no_of_nodes(root)
    
    def no_of_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Check if the tree is balanced or not
        leftChild_height = self.height_of_lefttree(root)
        rightChild_height = self.height_of_righttree(root)

        if leftChild_height == rightChild_height:
            """The Tree is Balanced"""
            return (2 ** rightChild_height) - 1 # (2^h) - 1
        else:
            """The Tree is Not Balanced"""
            leftChild_nodes = self.no_of_nodes(root.left)
            rightChild_nodes = self.no_of_nodes(root.right)
        
        return 1 + leftChild_nodes + rightChild_nodes
    
    def height_of_lefttree(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height += 1
            root = root.left
        
        return height
    
    def height_of_righttree(self, root: Optional[TreeNode]) -> int:
        height=0
        while root:
            height += 1
            root = root.right
        
        return height
        
    