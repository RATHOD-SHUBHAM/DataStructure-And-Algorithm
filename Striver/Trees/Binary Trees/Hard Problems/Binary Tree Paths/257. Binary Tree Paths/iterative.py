# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.op = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        queue = [[root, str(root.val)]]

        while queue:
            cur_node, cur_path = queue.pop(0)

            # If leaf node
            if not cur_node.left and not cur_node.right:
                self.op.append(cur_path)
            
            # If not leaf node
            if cur_node.left:
                new_cur_path = cur_path + '->' + str(cur_node.left.val)
                queue.append([cur_node.left, new_cur_path])
            
            if cur_node.right:
                new_cur_path = cur_path + '->' + str(cur_node.right.val)
                queue.append([cur_node.right, new_cur_path])

        return self.op