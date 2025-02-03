# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
    
    def dfs(self, root):
        if not root:
            return True
        
        leftSubTree = self.dfs(root.left)
        # print("left: ",root.val, leftSubTree)
        rightSubTree = self.dfs(root.right)
        # print("left: ",root.val, rightSubTree)

        curTree = True
        if root.left:
            if root.left.val >= root.val:
                curTree = False
        if root.right:
            if root.val >= root.right.val:
                curTree = False

        # print("root: ", curTree)
        
        return leftSubTree and rightSubTree and curTree
    

"""
Problem with this solution is:

1. It is not checking the left and right subtree of the root node. It is only checking the left and right child of the root node.

Cosnider this example:

     5
    / \
   4   6
      / \
      3  7  

The solution will return True for this example. 

But the tree is not a valid BST.

The child tree of 6 byitself is valid BST But the root node 5. 
The solution fails to check the entire tree for a valid BST, 3 cannot be to the right of 5.

Hence the solution is wrong.

"""