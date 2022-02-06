# time = O(n)
# space = O(h)

def allKindsOfNodeDepths(root,depthSum = 0, depth = 0):
    if root is None:
		return 0
	
	print(root.value)
	print("depth : ",depth)
	depthSum += depth
	print("depthSum : ",depthSum)
	
	print(depthSum + 
		allKindsOfNodeDepths(root.left, depthSum ,depth+1) + 
		allKindsOfNodeDepths(root.right , depthSum, depth+1))
	print("\n")
	return(
		depthSum + 
		allKindsOfNodeDepths(root.left, depthSum ,depth+1) + 
		allKindsOfNodeDepths(root.right , depthSum, depth+1)
	)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
