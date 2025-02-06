# Controlled Inorder Traversal.

# only considering next and has next
# Tc: O(1) | Sc: O(n)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder_left(root)
    
    def inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.inorder_left(node.right)
        return node.val

        

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()