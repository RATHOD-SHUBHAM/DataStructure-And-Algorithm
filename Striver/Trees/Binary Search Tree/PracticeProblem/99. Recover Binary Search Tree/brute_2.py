"""
Brute Force -> Brute Force 2:

    Get the inorder traversal of the tree and instead of sorting them
    Get the 2 swapped value

    Traverse the tree again if we find the value x swap it with y and vise versa
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_array = []

        self.x = None
        self.y = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorderTraversal(root)
        self.find_two_swapped()

        count = 2
        self.changeValue(root, count)
        return root
    
    def inorderTraversal(self, root):
        if not root:
            return
        
        self.inorderTraversal(root.left)

        self.inorder_array.append(root.val)

        self.inorderTraversal(root.right)
    
    def find_two_swapped(self):
        n = len(self.inorder_array)

        for i in range(n-1):
            if self.inorder_array[i+1] < self.inorder_array[i]:
                self.y = self.inorder_array[i+1]

                # The first swap occurrence
                if self.x == None:
                    self.x = self.inorder_array[i]
                # The second swap occurrence
                else:
                    break
    
    def changeValue(self, root, count):
        if not root:
            return
        
        if root.val == self.x:
            root.val = self.y
            count -= 1
        elif root.val == self.y:
            root.val = self.x
            count -= 1
        
        self.changeValue(root.left, count)
        self.changeValue(root.right, count)
