# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If level == len(op):
    Then this node is being encounterd for the first time
'''
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []
        queue = [[root, 0]] # Node, level

        while queue:
            node, level = queue.pop(0)

            if level == len(op):
                op.append(node.val)
            
            # Go right and then go left
            if node.right:
                queue.append([node.right, level + 1])
            
            if node.left:
                queue.append([node.left, level + 1])
        
        return op