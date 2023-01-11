# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p ,q)])
        return self.inorder(queue)
    
    def inorder(self, queue):
        while len(queue) > 0:
            root1 , root2 = queue.popleft()
            
            if not root1 and not root2:
                continue
        
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            queue.append((root1.left, root2.left))
            queue.append((root1.right, root2.right))
        
        return True
        