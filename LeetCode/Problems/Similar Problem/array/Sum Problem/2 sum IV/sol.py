'''

653. Two Sum IV - Input is a BST
Easy


Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105


# time: O(n) | space: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sorted_array = []
        self.inorder(root, sorted_array)
        
        # once I have a sorted array. perform 2 sum
        left = 0
        right = len(sorted_array) - 1
        
        while left < right:
            cur_sum = sorted_array[left] + sorted_array[right]
            
            if cur_sum > k:
                right -= 1
            elif cur_sum < k:
                left += 1
            else:
                return True
        
        return False
        
    def inorder(self, root, sorted_array):
        # base case
        if not root:
            return
        
        self.inorder(root.left, sorted_array)
        sorted_array.append(root.val)
        self.inorder(root.right, sorted_array)
        
        return sorted_array