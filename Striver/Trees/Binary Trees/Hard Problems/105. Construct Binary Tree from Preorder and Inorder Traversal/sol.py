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

        # build the left and right subtree: Root -> Left -> Right
        root.left = self.construct(start, root_idx - 1, inorder_dict, preorder)
        root.right = self.construct(root_idx + 1, end, inorder_dict, preorder)

        return root




# -------------------- Same solution but without dictionary --------------------
"""
Study the dictionary approach and then try to implement this
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        start = 0
        end = n - 1

        return self.BST(start, end, preorder, inorder)
    
    def BST(self, start, end, preorder, inorder):
        if start > end:
            return 
        
        root_val = preorder[self.idx]
        self.idx += 1

        root = TreeNode(root_val)

        root_idx = inorder.index(root_val)

        root.left = self.BST(start, root_idx - 1, preorder, inorder)
        root.right = self.BST(root_idx + 1, end, preorder, inorder)

        return root