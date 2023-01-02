def iterativeInOrderTraversal(tree, callback):
    # res = []
	curNode = tree
	prevNode = None
	nextNode = None
	
	while curNode:
		if not curNode.left:
			# res.append(curNode.value)
			callback(curNode)
			curNode = curNode.right
			
		else:
			nextNode = curNode.left
			
			while nextNode.right:
				nextNode = nextNode.right
				
			nextNode.right = curNode
			
			prevNode = curNode
			curNode = curNode.left
			prevNode.left = None		
