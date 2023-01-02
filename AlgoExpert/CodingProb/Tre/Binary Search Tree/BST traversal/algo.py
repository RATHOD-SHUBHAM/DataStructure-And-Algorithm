# time and space = O(n) || O(n)
def inOrderTraverse(tree, array):
    # Write your code here.
    if tree:
		# left
		inOrderTraverse(tree.left , array)
		# root
		array.append(tree.value)
		# right
		inOrderTraverse(tree.right, array)
		
	return array

def preOrderTraverse(tree, array):
    # Write your code here.
    if tree:
		# root
		array.append(tree.value)
		# left
		preOrderTraverse(tree.left, array)
		# right
		preOrderTraverse(tree.right, array)
	return array
		


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array
