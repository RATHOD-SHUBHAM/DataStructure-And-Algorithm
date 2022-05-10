# Node creation
class TreeNode:
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# left -> root -> right
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val,end = "")
    inorder(root.right)


# root -> left -> right
def preorder(root):
    if not root:
        return

    print(root.val, end = "")
    preorder(root.left)
    preorder(root.right)


# left -> right -> root
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val, end = "")


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder Traversal is: ")
    inorder(root)

    print("preorder traversal is: ")
    preorder(root)

    print("postorder traversal is: ")
    postorder(root)

    print("\n")

'''
        1
      /   \ 
     2      3
    / \     
   4   5   

'''