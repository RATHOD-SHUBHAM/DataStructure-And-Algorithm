from collections import deque


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root):
    if not root:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val)


        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("levelOrder Traversal is: ")
    levelOrderTraversal(root)