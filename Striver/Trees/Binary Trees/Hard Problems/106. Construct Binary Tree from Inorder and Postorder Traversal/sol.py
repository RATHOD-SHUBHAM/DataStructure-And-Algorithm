# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.idx = 0

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)

        self.idx = n - 1
        
        start = 0
        end = n - 1

        inorder_dict = {value : idx for idx, value in enumerate(inorder)}

        return self.construct_tree(start, end, inorder_dict, postorder)
    
    def construct_tree(self, start, end, inorder_dict, postorder):
        if start > end:
            return 
        
        root_val = postorder[self.idx]
        self.idx -= 1

        root = TreeNode(root_val)
        root_idx = inorder_dict[root_val]

        # build the right and left subtree: Left -> Right -> Root 
        root.right = self.construct_tree(root_idx + 1, end, inorder_dict, postorder)
        root.left = self.construct_tree(start, root_idx - 1, inorder_dict, postorder)
        

        return root


        