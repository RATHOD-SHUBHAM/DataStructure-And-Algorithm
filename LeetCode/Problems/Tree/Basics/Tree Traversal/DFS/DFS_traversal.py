class Solution:
    def inorder(self, root):
        op = []
        stack = []

        while root or len(stack) > 0:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            op.append(node.val)
            root = node.right

        return op

    def postOrder(self, root):
        if not root:
            return []

        op = []
        stack = [root]

        while stack:
            node = stack[-1]

            if not node.left and not node.right:
                op.append(node.val)

            if node.right:
                stack.append(node.right)
                node.right = None
            
            if node.left:
                stack.append(node.left)
                node.left = None

        return op
    
    def preOrder(self, root):
        if not root:
            return []

        op = []
        stack = [root]

        while stack:
            node = stack.pop()

            op.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
                
        return op


