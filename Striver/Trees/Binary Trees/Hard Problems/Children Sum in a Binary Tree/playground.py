# Top to bottom

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code here
        if not root:
            return 0
        
        return self.topDown(root)
    
    def topDown(self, root):
        if not root.left and not root.right:
            return 1
        
        leftVal = 0 if not root.left else root.left.data
        rightVal = 0 if not root.right else root.right.data
        
        if root.data != leftVal + rightVal:
            return 0
        else:
            leftTree = self.topDown(root.left)
            rightTree = self.topDown(root.right)
            
            return leftTree and rightTree
        

if __name__ == '__main__':
    root = Node(35)
    root.left = Node(20)
    root.right = Node(15)
    root.left.left = Node(15)
    root.left.right = Node(5)
    root.right.left = Node(10)
    root.right.right = Node(5)


    root = Node(10)
    root.left = Node(10)


    # root = Node(20)
    # root.left = Node(8)
    # root.right = Node(12)
    # root.right.left = Node(3)
    # root.right.right = Node(9)
    
    # root = Node(20)
    # root.left = Node(8)
    # root.right = Node(12)
    # root.left.left = Node(3)
    # root.left.right = Node(5)
    # root.right.left = Node(3)
    # root.right.right = Node(9)
    
    sol = Solution()
    print(sol.isSumProperty(root))
    
    # print(sol.topDown(root))
