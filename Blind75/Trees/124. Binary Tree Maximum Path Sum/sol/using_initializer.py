# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_sum = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.calculate_sum(root)
        return self.max_sum
    
    def calculate_sum(self, root):
        if not root:
            return 0

        leftTree_sum = self.calculate_sum(root.left)
        rightTree_sum = self.calculate_sum(root.right)


        # handiling negative values: If any of the subtree node has negative value, Then we donot consider that. So instead of negative number we take 0.

        leftTree_sum = max(leftTree_sum , 0)
        rightTree_sum = max(rightTree_sum , 0)
        
        # calculate the current sum
        cur_sum = root.val + leftTree_sum + rightTree_sum


        self.max_sum = max(self.max_sum , cur_sum)

        # return one path along with root
        return root.val + max(leftTree_sum , rightTree_sum)