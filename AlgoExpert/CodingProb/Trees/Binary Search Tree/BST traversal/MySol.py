# Time and space = O(n) || O(n)

def inOrderTraverse(tree, array):
    # Left root right
    if not tree.left and not tree.right:
		array.append(tree.value)
		return array
	
	# left
	if tree.left:
		inOrderTraverse(tree.left,array)
		
	# root
	array.append(tree.value)
	
	# right
	if tree.right:
		inOrderTraverse(tree.right,array)
	
	return array
	


def preOrderTraverse(tree, array):
    # root left right
	
	if not tree.left and not tree.right:
		array.append(tree.value)
		return array
	
	# root
	array.append(tree.value)
	
	# left
	if tree.left:
		preOrderTraverse(tree.left, array)
	
	# right
	if tree.right:
		preOrderTraverse(tree.right, array)
		
	return array


def postOrderTraverse(tree, array):
    # Left Right Root.
	
	if not tree.left and not tree.right:
		array.append(tree.value)
		return array
	
	# left
	if tree.left:
		postOrderTraverse(tree.left, array)
	#right
	if tree.right:
		postOrderTraverse(tree.right, array)
	
	array.append(tree.value)
	
	return array
