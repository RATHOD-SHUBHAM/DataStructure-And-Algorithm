class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        # first get the inorder array
        inorder_Array = self.inorder(root)
        print(inorder_Array)

        # construct binary search tree
        n = len(inorder_Array)
        start = 0
        end = n - 1
        return self.BST(inorder_Array, start, end)


    def inorder(self, root):
        op = []
        stack = []

        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            curNode = stack.pop()
            op.append(curNode.value)
            curNode = curNode.right

        return op



    def BST(self, array, start, end):
        
        if end < start:
            return

        mid = start + (end - start) // 2
        mid_node = array[mid]
        root = BT(mid_node)

        root.left = self.BST(array, start, mid - 1)
        root.right = self.BST(array, mid + 1, end)

        return root

    def printBST(self, root):
        # perform preorder traversal
        if not root:
            return None

        op = []
        stack = [root]

        while stack:
            node = stack.pop()

            op.append(node.value)
            
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return op


if __name__ == '__main__':
    #            10
    #           /
    #          8
    #         /
    #        7
    #       /
    #      6
    #     /
    #    5
    root = BT(10)
    root.left = BT(8)
    root.left.left = BT(7)
    root.left.left.left = BT(6)
    root.left.left.left.left = BT(5)

    obj = Solution()
    BST = obj.convertBST(root)
    
    op = obj.printBST(BST)
    print(op)