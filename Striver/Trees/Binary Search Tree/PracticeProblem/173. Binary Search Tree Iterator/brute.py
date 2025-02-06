# Flatten the tree.
# Tc: O(n) | Sc: O(n)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        
        self.inorder_traversal(root)
        
        self.n = len(self.inorder)

        self.ptr = -1
    
    def inorder_traversal(self, root):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            self.inorder.append(node.val)

            root = node.right

    def next(self) -> int:
        # Moves the pointer to the right, then returns the number at the pointer.
        self.ptr += 1
        return self.inorder[self.ptr]

    def hasNext(self) -> bool:
        #  Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
        if self.ptr + 1 < self.n:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()