# --------------------------------------- Recursive  ---------------------------------------

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        leftChild = root.left
        rightChild = root.right

        return self.helper(leftChild, rightChild)
    
    def helper(self, leftChild, rightChild):
        if leftChild and rightChild: # is not None
            return leftChild.val == rightChild.val and self.helper(leftChild.left,rightChild.right) and self.helper(leftChild.right,rightChild.left)
        
        if (not leftChild and rightChild) or (leftChild and not rightChild):
            return False
        else:
            return True



# --------------------------------------- Iterative ---------------------------------------

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        
        if not root.left or not root.right:
            return False
        
        queue = [root.left, root.right]

        while queue:
            node_one = queue.pop(0)
            node_two = queue.pop(0)

            if not node_one and not node_two:
                continue

            if not node_one or not node_two:
                return False
        
            
            if node_one.val != node_two.val:
                return False

            
            # node_one -> Left child, node_two -> Right Child
            queue.append(node_one.left)
            queue.append(node_two.right)

            # node_one -> Right child, node_two -> Left Child
            queue.append(node_one.right)
            queue.append(node_two.left)

        
        return True
