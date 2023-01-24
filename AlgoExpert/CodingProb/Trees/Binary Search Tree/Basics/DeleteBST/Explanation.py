'''
# Delete a node in BST

## Deletion of a node in BST has 2 major step:
1. Search -- for the value.
2. Remove -- the value. #has 2 case

## Removal has 2 Case in it:
1. When the root has 2 subtree.
2. When root node has only one subtree.

## Case 1: When the root has 2 subtree.
### Rule
1. Take the smallest value node from the right subtree. ie, left most node of the right subtree.
2. Now replace the curNode with this smallest node

## Case 2: When root node has only one subtree, has 3 scenario:
1. When we have to delete the root node.
2. when we have to delete a node in between.
3. when there is only one node.

'''

# O(n) time || O(1) space

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
            #step1:  searching
            if value < curNode.val:
                parentNode = curNode
                curNode = curNode.left
            elif value > curNode.val:
                parentNode = curNode
                curNode = curNode.right
            else: # the value is found
                # case 1: when the node has 2 subtree
                if curNode.left and curNode.right:
                    curNode.val = self.getMin(curNode.right) # find the smallest node from right subtree
                    self.helper(curNode.right,curNode.val,curNode) # remove the node
                else: #node has only one subtree
                    if parentNode is None: # scenario1: root node has to be deleted
                        if curNode.left:
                            curNode.val = curNode.left.val
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left
                        elif curNode.right:
                            curNode.val = curNode.right.val
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right
                        else:
                            return #if the node is the only ndoe
                    
					# if we have to delete a node in between
                    elif parentNode.left == curNode:
                        parentNode.left = curNode.left if curNode.left is not None else curNode.right
                    elif parentNode.right == curNode:
                        parentNode.right = curNode.right if curNode.right else curNode.left
                    break
        return root
    
	# gives the smallest node from the right subtree
    def getMin(self,node):
        curNode = node
        
        while curNode.left:
            curNode = curNode.left
        return curNode.val