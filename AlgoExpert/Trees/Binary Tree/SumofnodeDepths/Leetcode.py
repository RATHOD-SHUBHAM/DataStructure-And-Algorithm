# Slightly different question from leetcode

'''

104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


'''
# O(n) time | O(h) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        depth = 1
        stack = deque([ (depth,root) ])
        
        
        while stack:
            cur_depth , root = stack.popleft()
            depth = max(cur_depth , depth)
            
            children = [root.left, root.right]
            
            if not any(children):
                continue
            
            for child in children:
                if child:
                    stack.append((cur_depth+1, child))
                    
        return depth