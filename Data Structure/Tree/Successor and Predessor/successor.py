# Successor is the next element after a current node

# so for a given root element, The next value will be left most child of the right subtree
class Solution:
    def successor(self, root):
        root = root.right

        while root.left:
            root = root.left

        return root.val

        