# Tc :O(m + n) | Sc: max(O(h1 + h2))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack_1 = [root1]
        stack_2 = [root2]
        
        while len(stack_1) > 0 and len(stack_2) > 0:
            # get the leaf node from both the tree
            leafNode_1 = self.getLeafNode(stack_1)
            leafNode_2 = self.getLeafNode(stack_2)
            
            # compare the leaf nodes
            if leafNode_1.val != leafNode_2.val:
                return False
        
        return True if len(stack_1) == 0 and len(stack_2) == 0 else False
    
    
    def getLeafNode(self, stack):
        node = stack.pop()
        
        # as long the given node is not leaf - keep traversing
        while not self.isLeaf(node): # check if the given node is a leaf node
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
            
            node = stack.pop()
            
        return node
    
    def isLeaf(self, node):
        if not node.left and not node.right:
            return True
        else:
            return False