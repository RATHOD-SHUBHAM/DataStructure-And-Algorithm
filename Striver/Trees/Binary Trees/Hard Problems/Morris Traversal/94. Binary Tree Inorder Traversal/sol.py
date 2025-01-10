# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        op = []

        cur_node = root
        
        # Left >> Root >> Right
        while cur_node:
            # If there is no left node - append root and move right
            if not cur_node.left:
                op.append(cur_node.val)
                cur_node = cur_node.right
            
            # If left child exist
            else:
                child_node = cur_node.left

                # Grab the right most node of child node
                while child_node.right is not None and child_node.right != cur_node:
                    child_node = child_node.right
                
                # Check if there is a thread or not
                if child_node.right == None:
                    # there is no thread - so create a thread and move left
                    child_node.right = cur_node
                    cur_node = cur_node.left
                
                else:
                    # thread is found - break the thread
                    child_node.right = None
                    op.append(cur_node.val)
                    cur_node = cur_node.right

        return op

                
