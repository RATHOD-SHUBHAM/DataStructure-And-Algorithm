# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        queue = [root]
        
        
        while queue:
            
            # for every level add a block
            res.append([])
            
            # get the len of parents nodes
            q_len = len(queue)
            
            for i in range(q_len):
                node = queue.pop(0)
                
                # add the node to current level
                res[-1].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)                
            
        # print(res)
        return res