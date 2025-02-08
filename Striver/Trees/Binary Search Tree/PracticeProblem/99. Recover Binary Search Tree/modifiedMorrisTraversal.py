# Slightly Modified version of Morris Traversal to find the two nodes that are swapped.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.pred = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:

        curNode = root

        while curNode:

            if not curNode.left:
                if self.pred and curNode.val < self.pred.val:
                    self.y = curNode

                    if self.x == None:
                        self.x = self.pred
                    # else:
                    # If we break before completing the traversal, some of these temporary connections remain in place causing tree structure to go wrong.
                    #     break
                    
                self.pred = curNode

                curNode = curNode.right

            else:
                childNode = curNode.left

                while childNode.right and childNode.right != curNode:
                    childNode = childNode.right

                
                if childNode.right == None:
                    childNode.right = curNode
                    curNode = curNode.left
                
                else:
                    if self.pred and curNode.val < self.pred.val:
                        self.y = curNode

                        if self.x == None:
                            self.x = self.pred
                        # else:
                        # If we break before completing the traversal, some of these temporary connections remain in place causing tree structure to go wrong and could go into inifinte loop
                        #     break
                    
                    
                    self.pred = curNode
                    
                    childNode.right = None
                    curNode = curNode.right
            
        # Swap the values
        self.x.val, self.y.val = self.y.val, self.x.val

        return root