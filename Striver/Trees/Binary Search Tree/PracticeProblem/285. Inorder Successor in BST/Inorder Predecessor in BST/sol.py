# Using BST property

# Tc: O(n) | Sc: O(1)

'''
Inorder property: Left , root , right

When we write inorder in BST we get a sorted array

If my p <= root:
    then predecessor wont be on right side, it will be on left side

But if p > root:
    Then this root can be a potential predecessor, left -> root
    Then move right
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderPredecessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        node = root
        predecessor = None

        while node:
            if p.val <= node.val:
                # Move left: This node cant be a predecessor nor anybody on the right
                node = node.left
            else:
                # This node can be a potential successor
                predecessor = node
                node = node.right
        
        return predecessor