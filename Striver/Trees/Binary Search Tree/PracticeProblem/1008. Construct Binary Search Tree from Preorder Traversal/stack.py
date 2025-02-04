# Tc and Sc: O(n)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        root_val = preorder[0]
        root = TreeNode(root_val)

        stack = [root]

        for i in range(1, n):
            child_val = preorder[i]

            node = stack[-1]
            child = TreeNode(child_val)

            while stack and stack[-1].val < child.val:
                # Remove all the node that are smaller to the child node
                node = stack.pop()
                
            
            if node.val < child.val:
                # add the right child
                node.right = child
            elif node.val > child.val:
                # add the left child
                node.left = child
            
            stack.append(child)
        
        return root