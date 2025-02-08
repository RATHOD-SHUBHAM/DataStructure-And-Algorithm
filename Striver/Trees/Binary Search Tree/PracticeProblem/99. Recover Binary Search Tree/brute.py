"""
Brute Force:

    Get the inorder traversal of the tree and sort them
    Rule: The BST inorder is always sorted

    Traverse the tree again in inorder fashion and then compare the values with that of sorted array
    if the values dont match, replace the value.

    In this way we will have all the values in right order
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_array = []
        self.ptr = 0

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorderTraversal(root)
        self.inorder_array.sort()

        self.changeValue(root)
        return root
    
    def inorderTraversal(self, root):
        if not root:
            return
        
        self.inorderTraversal(root.left)

        self.inorder_array.append(root.val)

        self.inorderTraversal(root.right)
    
    def changeValue(self, root):
        curNode = root

        stack = []

        while curNode or stack:
            while curNode :
                stack.append(curNode)
                curNode = curNode.left
            
            node = stack.pop()

            if node.val != self.inorder_array[self.ptr]:
                node.val = self.inorder_array[self.ptr]
            
            self.ptr += 1

            curNode = node.right

        