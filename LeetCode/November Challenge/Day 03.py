'''

129. Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.


'''

'''

Time Complexity = O(n) // where n is the number of elements in the tree.
Space Complexity = O(1) // no additional memory is being used

# https://www.youtube.com/watch?v=Jk16lZGFWxE

Approach:

Go to the root node.
Add the root node to units place --> can be done by multiplying existing number to 10 and adding current value

Check if it has right and left child.

if it does continue the same above approach
else return the sum

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def helper(root, num):
            
            # base case checking
            if not root:
                return 0
            
            
            # if there is any value then add it to num variable
            num = num * 10 + root.val
            
            
            # if there is no child then return num
            if not root.left and not root.right:
                return num
            
            return helper(root.left,num) + helper(root.right,num)
        
        return helper(root,0)
        
        