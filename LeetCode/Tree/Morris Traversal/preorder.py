class TreeNode:
    def __init__ (self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    curNode = root

    while curNode:
        if not curNode.left:
            print(curNode.val , end = "")
            curNode = curNode.right

        else:
            nextNode = curNode.left

            while nextNode.right != None and nextNode.right != curNode:
                nextNode = nextNode.right

            # this means the node is been visited the first time
            if nextNode.right is None:
                print(curNode.val , end = "")
                nextNode.right = curNode
                curNode = curNode.left
            # node has already been visited
            elif nextNode.right is curNode:
                nextNode.right = None
                curNode = curNode.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    preorder(root)


'''
        1
      /   \ 
     2      3
    / \     
   4   5   

'''