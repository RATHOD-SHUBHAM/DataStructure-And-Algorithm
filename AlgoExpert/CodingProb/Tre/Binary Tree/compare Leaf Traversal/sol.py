# same as leet code

# time = O(m+n) where m is the number of nodes in the tree and n is the number of nodes in the tree
# space = O(l1 + l2) where l1 and l2 is the list used to store leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []
        self.helper(root1,leaf1)
        self.helper(root2, leaf2)
        return leaf1 == leaf2
        
        
    def helper(self,node,leaf):
        if node:
            if not node.left and not node.right:
                leaf.append(node.val)

            self.helper(node.left,leaf)
            self.helper(node.right,leaf)

        