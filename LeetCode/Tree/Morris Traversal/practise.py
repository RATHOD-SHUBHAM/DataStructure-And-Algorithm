# https://www.youtube.com/watch?v=80Zug6D1_r4&t=1224s


class TreeNode:
    def __init__(self, val , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    pass


def preorder(root):
    pass


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    inorder(root)

    preorder(root)

'''
        1
      /   \ 
     2      3
    / \     
   4   5   

'''