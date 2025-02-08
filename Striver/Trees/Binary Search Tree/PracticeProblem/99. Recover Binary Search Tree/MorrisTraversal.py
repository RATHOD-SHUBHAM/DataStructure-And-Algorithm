# Morris Traversal -> Inorder.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        op = []

        curNode = root

        while curNode:
            if not curNode.left:
                op.append(curNode.val)
                curNode = curNode.right
            else:
                childNode = curNode.left

                while childNode.right and childNode.right != curNode:
                    childNode = childNode.right

                
                if childNode.right == None:
                    childNode.right = curNode
                    curNode = curNode.left
                
                else:
                    op.append(curNode.val)
                    childNode.right = None
                    curNode = curNode.right
            
        print(op)


