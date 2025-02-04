# Valid BST.

# Tc: O(N) | Sc: O(N)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.idx = 0

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        minRange = -math.inf
        maxRange = math.inf
        return self.validBST(minRange, maxRange, preorder, n)
    
    def validBST(self, minRange, maxRange, preorder, n):
        if self.idx == n:
            return None
        
        node_val = preorder[self.idx]

        # Validate
        if node_val <= minRange or node_val >= maxRange:
            return None

        # Create node
        self.idx += 1
        root = TreeNode(node_val)

        root.left = self.validBST(minRange, node_val, preorder, n)
        root.right = self.validBST(node_val, maxRange, preorder, n)

        return root


        