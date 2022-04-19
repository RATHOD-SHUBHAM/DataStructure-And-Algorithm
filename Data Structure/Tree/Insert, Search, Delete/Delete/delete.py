# Time = O(logN)
# Space = O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root,key)
    
    def delete(self, root, val, parentNode = None):
        curNode = root
        
        while curNode:
            # searching
            if val < curNode.val:
                parentNode = curNode
                curNode = curNode.left
            elif val > curNode.val:
                parentNode = curNode
                curNode = curNode.right
                
            else:
                # if both child exist
                if curNode.left and curNode.right:
                    curNode.val = self.getMin(curNode.right)
                    self.delete(curNode.right, curNode.val, curNode)
                
                # only one child exist
                else:
                    if not parentNode:
                        if curNode.left:
                            curNode.val = curNode.left.val
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left
                        elif curNode.right:
                            curNode.val = curNode.right.val
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right
                        # when there is no parent and no child
                        else:
                            return
                        
                    elif parentNode.left == curNode:
                        parentNode.left = curNode.left if curNode.left else curNode.right
                    elif parentNode.right == curNode:
                        parentNode.right = curNode.right if curNode.right else curNode.left
                    
                    break
                    
        return root
                    
        
    def getMin(self, node):
        curNode = node
        
        while curNode.left:
            curNode = curNode.left
            
        return curNode.val
                