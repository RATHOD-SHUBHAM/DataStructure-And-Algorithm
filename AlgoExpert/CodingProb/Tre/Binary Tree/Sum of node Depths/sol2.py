'''
formula = 

f(node,depth) = depth + f(left ,depth+1) + f(right,depth+1)


						  0
					/			\
					2				3
				/		\		/		\
				4		5		6		7
				
root = 0
f(0,0) = 0 + f(left,d+1) + f(right,d+1)

f(left) = 2
d+1 = 1
f(2,1) = 1 + f(left,d+1) + f(right,d+1)
             /
f(left) = 4												
d+1 = 2
f(4,2) = 2 + f(left,d+1) + f(right,d+1)
				/				/
f(left) = None				f(Right) = None


'''
# O(n) time | O(h) space
def nodeDepths(root,depth = 0):
	if root is None:
		return 0 # if there is no root node then the depth of the node is Zero.
	return depth + nodeDepths(root.left, depth +  1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
