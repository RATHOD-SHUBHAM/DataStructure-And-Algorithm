class Solution:
    def predessor(self, root):
        root = root.left

        while root.right:
            root = root.right

        return root.val

        