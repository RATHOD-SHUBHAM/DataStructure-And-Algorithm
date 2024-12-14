# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node):
        '''Check if the node is a leaf node or not'''
        if not node.left and not node.right:
            return True
        else:
            return False

    def left_boundary(self, root):
        """Return all the left side nodes except leaf node"""
        if not root.left:
            return []
        
        cur_node = root.left
        op = []

        while cur_node:
            # check for leaf nodes
            if not self.isLeaf(cur_node):
                op.append(cur_node.val)

            if cur_node.left:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        
        return op

    def leaf_nodes(self, root, leaves):
        """Get all the leaf nodes from left to right"""
        if self.isLeaf(root):
            leaves.append(root.val)
            return

        if root.left:
            self.leaf_nodes(root.left, leaves)
        
        if root.right:
            self.leaf_nodes(root.right, leaves)
        

        


    def right_boundary(self, root):
        """Return all the right side nodes except leaf node"""
        if not root.right:
            return []
        
        cur_node = root.right
        op = []

        while cur_node:
            # check for leaf nodes
            if not self.isLeaf(cur_node):
                op.append(cur_node.val)

            if cur_node.right:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        
        return op[::-1]

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        op.append(root.val)
        
        # Left Boundary
        op_left_boundary = self.left_boundary(root)
        op = op + op_left_boundary
        # print(op)
        
        # Leaf Nodes
        leaves = []
        if not self.isLeaf(root):
            # if root itself is not a leaf node
            self.leaf_nodes(root, leaves)
            op = op + leaves
        # print(op)


        # Right Boundary
        op_right_boundary = self.right_boundary(root)
        op = op + op_right_boundary
        # print(op)

        return op