# ------------------------------ Brute Force ------------------------------

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



# -------------------------- Better Brute Force --------------------------

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
            # This is the logic that will be used in next 2 solution
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


# ------------------------------ Better Recursive ------------------------------

"""
Using the same find 2 swapped algorithm
"""
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
        self.inorderTraversal(root)

        # Swap the values
        self.x.val , self.y.val = self.y.val, self.x.val

        return root
    
    def inorderTraversal(self, root):
        if not root:
            return
        
        self.inorderTraversal(root.left)

        # Check if nums[i-1] > nums[i]
        if self.pred and root.val < self.pred.val:
            self.y = root

            if self.x == None:
                self.x = self.pred
            else:
                return

        self.pred = root

        self.inorderTraversal(root.right)

# ------------------------------ Better Iterative ------------------------------

"""
Using the same find 2 swapped algorithm
"""
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
        self.inorderTraversal(root)

        # Swap the values
        self.x.val , self.y.val = self.y.val, self.x.val

        return root
    
    def inorderTraversal(self, root):
        curNode = root
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()

            # Check if nums[i-1] > nums[i]
            if self.pred and node.val < self.pred.val:
                self.y = node

                if self.x == None:
                    self.x = self.pred
                else:
                    break
            
            self.pred = node

            root = node.right
        
        return
    
# ------------------------------ Morris Traversal ------------------------------
"""
In threaded Binary Tree, we add a thread from previous node to current node.

We can use this logic to check
if nums[i-1] > nums[i]
"""

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
