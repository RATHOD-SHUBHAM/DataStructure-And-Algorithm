# Inorder Preorder Construction

# Tc: O(nlogn) + O(n) | Sc: O(1)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preorder_idx = 0
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        inorder = sorted(preorder)

        inorder_dict = {val : idx for idx, val in enumerate(inorder)}

        start = 0
        end = n - 1

        return self.construct(start, end, preorder, inorder_dict)
    
    def construct(self, start, end, preorder, inorder_dict):
        if start > end:
            return
        
        root_val = preorder[self.preorder_idx]
        self.preorder_idx += 1

        root = TreeNode(root_val)

        root_idx = inorder_dict[root_val]

        root.left = self.construct(start, root_idx - 1, preorder, inorder_dict)
        root.right = self.construct(root_idx + 1, end, preorder, inorder_dict)

        return root