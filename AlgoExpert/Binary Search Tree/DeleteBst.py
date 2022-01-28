'''

450. Delete Node in a BST
Medium

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []

'''
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/1725214/Python-oror-Step-by-Step-Explanation-oror-O(n)-time-oror-O(1)-space-oror-Easy-To-Understand.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        value = key
        return self.helper(root,value)
    
    def helper(self,root,value,parentNode = None):
        curNode = root
        
        while curNode:
            # searching
            if value < curNode.val:
                parentNode = curNode
                curNode = curNode.left
            elif value > curNode.val:
                parentNode = curNode
                curNode = curNode.right
            else: # the value is found
                # case 1: when the node has 2 child
                if curNode.left and curNode.right:
                    curNode.val = self.getMin(curNode.right)
                    self.helper(curNode.right,curNode.val,curNode)
                else:
                    if parentNode is None:
                        if curNode.left:
                            curNode.val = curNode.left.val
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left
                        elif curNode.right:
                            curNode.val = curNode.right.val
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right
                        else:
                            return
                    
                    elif parentNode.left == curNode:
                        parentNode.left = curNode.left if curNode.left is not None else curNode.right
                    elif parentNode.right == curNode:
                        parentNode.right = curNode.right if curNode.right else curNode.left
                    break
        return root
    
    def getMin(self,node):
        curNode = node
        
        while curNode.left:
            curNode = curNode.left
        return curNode.val