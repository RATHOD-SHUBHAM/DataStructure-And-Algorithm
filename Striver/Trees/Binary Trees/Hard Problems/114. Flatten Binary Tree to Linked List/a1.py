# --------------- Recursive Solution ---------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.prevNode = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.LL(root)

        return root
    
    def LL(self, root):
        if not root:
            return
        
        self.LL(root.right)
        self.LL(root.left)

        # Set the right pointer to right child
        root.right = self.prevNode

        # Set left child as None
        root.left = None

        # Set current node as prevNode
        self.prevNode = root

        return

# ------- Iterative Solution -------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]

        while stack:
            node = stack.pop()

            # Move frrom right to left
            if node.right:
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
            
            # Creat new tree
            node.left = None
            if stack:
                node.right = stack[-1]
        
        return root
    
#  ------- Threaded Solution -------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        curNode = root

        while curNode:
            if not curNode.left:
                curNode = curNode.right
            else:
                prevNode = curNode.left
                

                # Move to leftchild's rightmost node
                while prevNode.right:  
                    prevNode = prevNode.right
                
                # Connect the right node to leftchild's rightmost node
                prevNode.right = curNode.right

                # Move the leftchild to right
                curNode.right = curNode.left

                curNode.left = None
