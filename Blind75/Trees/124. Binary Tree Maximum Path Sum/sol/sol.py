'''
There are 2 case
case 1:
    1
   / \
  2   3
  In this case: Individual tree we have to calculate 2 + 1 + 3
  ie parent + left + right
  
case 2:
    1
   / \
  2   3
     / \
    4   5
In this case we have to calculate
    max of 3 cases
1. Individual tree = 4 + 3 + 5
2. Path 2 + 1 + 3 + 4
3. Path 2 + 1 + 3 + 5

from 1 path of 3 will-- max left or right child for node 3

# Catch:
if there is a negative number change that 0 [ignoring the node].
because eg: 3 -4 + 5 = 4 and 3 + 0 + 5 = 8

'''

# time and space = O(n)
# Space complexity: O(h), where h is a tree height, to keep the recursion stack. In the average case of balanced tree, the tree height h = log h, in the worst case of skewed tree, h = n.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [-math.inf]
        self.helper(root,max_path_sum)
        return max_path_sum[0]
    
    def helper(self, root, max_path_sum):
        if not root:
            return 0
        
        # get the path for left and right child
        leftChild = self.helper(root.left,max_path_sum)
        rightChild = self.helper(root.right,max_path_sum)
        
        # now check if the value is negative. 
        leftChild = max(leftChild, 0)
        rightChild = max(rightChild , 0)
        
        # calculate individual tree sum
        curTreeSum = root.val + leftChild + rightChild
        max_path_sum[0] = max(max_path_sum[0], curTreeSum)
        
        # for entire tree
        return root.val + max(leftChild, rightChild)