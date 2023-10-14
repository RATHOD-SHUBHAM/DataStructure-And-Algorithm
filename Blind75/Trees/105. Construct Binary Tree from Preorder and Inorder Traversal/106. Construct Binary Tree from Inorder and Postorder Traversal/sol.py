# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        left = 0
        right = len(postorder) - 1

        inorder_dict = {num:idx for idx , num in enumerate(inorder)}

        return self.construct(left, right, postorder, inorder_dict)

    def construct(self, left, right, postorder, inorder_dict):
        if left > right:
            return 
        
        # build the root node
        root_val = postorder.pop()
        root = TreeNode(root_val)
    
        # get the left and right subtree
        inorder_idx = inorder_dict[root_val]

        root.right = self.construct(inorder_idx + 1, right, postorder, inorder_dict)
        root.left = self.construct(left, inorder_idx - 1, postorder, inorder_dict)

        return root





        