# Node creation
class TreeNode:
    def __init__(self,val,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# left -> root -> right
def inorder(root):
    pass

# root -> left -> right
def preorder(root):
    pass


# left -> right -> root
def postorder(root):
    pass

def levelOrderTraversal(root):
    pass

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

    print("levelOrder Traversal is: ")
    levelOrderTraversal(root)

    print("\n")

'''
        1
      /   \ 
     2      3
    / \     
   4   5   

'''