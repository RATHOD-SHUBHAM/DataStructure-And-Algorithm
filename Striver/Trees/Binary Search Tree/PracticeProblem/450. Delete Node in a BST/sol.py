# https://www.youtube.com/watch?v=LFzAoJJt92M

"""
Steps:
    1. Find the node that needs to be deleted.
    2. For this node to be deleted: Get the right child's smallest value and replace it with the "value" of node to be deleted.

    Now repeate the same, find the right child's smallest value node and then remove the node

Note:
    * If the node has only left or only right child, then simply attach the parent node to current nodes left or the right child

    * When we loop the second time, we always have the leaf node value we are looking for


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parentNode = None
        return self.search_and_replace(root, key, parentNode)
    
    def search_and_replace(self, root, key, parentNode):
        curNode = root

        while curNode:
            if key < curNode.val:
                # Move left
                parentNode = curNode
                curNode = curNode.left
            elif key > curNode.val:
                # Move right
                parentNode = curNode
                curNode = curNode.right
            else:
                # if the node has both child: Get right child's smallest node(left most node)
                if curNode.left and curNode.right:
                    curNode.val = self.getMinVal(curNode.right)

                    # delete the right child's smallest node
                    self.search_and_replace(curNode.right, curNode.val, curNode)
                else:
                    # If there is only one child: Left or right

                    # case 1: If top most node is getting replaced
                    if parentNode == None:
                        if curNode.left:
                            curNode.val = curNode.left.val
                            # Make sure this is happens in order
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left

                        elif curNode.right:
                            curNode.val = curNode.right.val
                            # Make sure this is happens in order
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right

                        else:
                            return
                    
                    # Case 2: this is second iteration or removing leaf node, so this will have parent node
                    elif parentNode.left == curNode:
                        parentNode.left = curNode.left if curNode.left else curNode.right
                    elif parentNode.right == curNode:
                        parentNode.right = curNode.right if curNode.right else curNode.left
                    
                    # Now the node is replaced and leaf node is removed
                    break
        
        return root
    

    def getMinVal(self, node):
        while node.left:
            node = node.left
        return node.val