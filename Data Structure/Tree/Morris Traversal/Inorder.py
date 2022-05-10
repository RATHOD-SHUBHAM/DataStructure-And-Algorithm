# https://www.youtube.com/watch?v=80Zug6D1_r4&t=1224s


class TreeNode:
    def __init__(self, val , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    curNode = root

    while curNode:
        # if the curNode doesnot have any leftchild then print the current value and go right
        if not curNode.left:
            print(curNode.val , end = " ")
            curNode = curNode.right

        # if there is a left child
        else:
            nextNode = curNode.left

            # move to rightmost child of the left subtree
            while nextNode.right != None and nextNode.right != curNode:
                nextNode = nextNode.right


            # if nextnode.right is None then we have are visiting the node for the first time
            if nextNode.right is None:
                nextNode.right = curNode
                curNode = curNode.left

            # now if there is a pointer already from next node to curNode then we have already visited the left subtree
            elif nextNode.right == curNode:
                # make the right pointer point to none
                nextNode.right = None
                print(curNode.val, end = " ")
                curNode = curNode.right


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    inorder(root)

'''
        1
      /   \ 
     2      3
    / \     
   4   5   

'''