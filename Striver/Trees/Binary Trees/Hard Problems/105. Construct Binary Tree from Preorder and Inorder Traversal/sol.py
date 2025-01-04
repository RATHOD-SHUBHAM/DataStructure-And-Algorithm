# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preorder_idx = 0 # this should update and hold its position each time

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Index the nodes: Given an root, This will say about left and right subtree
        inorder_dict = {node : idx for idx, node in enumerate(inorder)}

        # Keep track of nodes
        start = 0
        end = len(preorder) - 1 # or inorder, anything as they have the same length

        return self.construct(start, end, inorder_dict, preorder)

    def construct(self, start, end, inorder_dict, preorder):
        # When there are no nodes
        if start > end:
            return
        
        # get the root and create a node
        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1

        root = TreeNode(root_val)

        # get the left and right subtree info of the current node
        root_idx = inorder_dict[root_val]

        # build the left and right subtree
        root.left = self.construct(start, root_idx - 1, inorder_dict, preorder)
        root.right = self.construct(root_idx + 1, end, inorder_dict, preorder)

        return root
