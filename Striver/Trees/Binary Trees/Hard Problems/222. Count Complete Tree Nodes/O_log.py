# Tc: O(log^2n) | Sc: O(1).

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.subtree_countNodes(root)
    
    def subtree_countNodes(self, root):
        if not root:
            return 0
        
        # leftChild_height = self.height(root.left)
        # rightChild_height = self.height(root.right)

        leftChild_height = self.left_height(root)
        rightChild_height = self.right_height(root)
        # print(leftChild_height, rightChild_height)


        if leftChild_height == rightChild_height:
            # no of nodes = 2^h - 1
            return (2 ** leftChild_height) - 1
        else:
            # Count the nodes
            left_subtree_node_count = self.subtree_countNodes(root.left)
            right_subtree_node_count = self.subtree_countNodes(root.right)

            return 1 + left_subtree_node_count + right_subtree_node_count
    

    def height(self, root):
        """This will only work for balanced binary tree"""
        if not root:
            return 0
        
        leftChild_height = self.height(root.left)
        rightChild_height = self.height(root.right)

        return 1 + max(leftChild_height, rightChild_height)
    
    # For complete binary tree we can count left most and right most nodes, if they are not same, then they are imbalanced
    def left_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def right_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height 
    
