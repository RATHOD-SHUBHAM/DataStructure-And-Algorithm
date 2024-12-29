# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val = max(nums)
        idx = nums.index(max_val)
        
        # Create a root node
        root = TreeNode(max_val)

        # Get the left child
        nums_left_half = nums[ : idx]
        root.left = self.constructMaximumBinaryTree(nums_left_half)

        # Get the right child
        nums_right_half = nums[idx+1 : ]
        root.right = self.constructMaximumBinaryTree(nums_right_half)

        return root
