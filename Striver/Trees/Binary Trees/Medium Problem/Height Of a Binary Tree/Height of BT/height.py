class BT:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def heightBST(root):
    if not root:
        return 0

    # get the hgiht of left and right sub tree
    leftTree_height = heightBST(root.left)
    rightTree_height = heightBST(root.right)

    # return height of tree
    # 1 : include the current node
    return 1 + max(leftTree_height , rightTree_height)

if __name__ == '__main__':
    root = BT(1)
    root.left = BT(2)
    root.right = BT(3)
    root.left.left = BT(4)
    root.left.right = BT(5)

    print(heightBST(root))