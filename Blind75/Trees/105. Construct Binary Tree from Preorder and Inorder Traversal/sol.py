# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        # this value should keep updating
        self.preorder_idx = 0 # just like nonlocal, value should be preserved

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # get index of nodes
        inorder_dict = {node:idx for idx, node in enumerate(inorder)}
        print(inorder_dict)

        left = 0
        right = len(preorder) - 1

        # preorder_idx = 0

        return self.construct(left, right, inorder_dict, preorder)
    
    def construct(self, left, right, inorder_dict, preorder):

        # When there is no node
        if left > right:
            return None
        
        # construct node
        root_val = preorder[self.preorder_idx]
        root = TreeNode(root_val)

        self.preorder_idx += 1

        # get the left and right subtree of current root from inorder array
        cur_root_idx = inorder_dict[root_val]

        # move left and right
        root.left = self.construct(left, cur_root_idx - 1, inorder_dict, preorder)

        root.right = self.construct(cur_root_idx + 1, right, inorder_dict, preorder)

        return root
        
