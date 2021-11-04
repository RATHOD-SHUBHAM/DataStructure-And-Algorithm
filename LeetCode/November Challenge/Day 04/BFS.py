'''

404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#BFS
from collections import deque

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        q = deque([root])
        
        while q:
            # step 1 : Pop the element out of queue
            node = q.popleft()
            
            # step 2: we will check if the node has left and right child
            # if yes we will add it to our queue
            # and then check if the left child is our leaf node or not
            
            if node.left:
                # add it to the queue
                q.append(node.left)
                
                # step 3: Check if the left node is a leaf node
                if not node.left.left and not node.left.right:
                    res += node.left.val
            
            if node.right:
                q.append(node.right)
                
        return res