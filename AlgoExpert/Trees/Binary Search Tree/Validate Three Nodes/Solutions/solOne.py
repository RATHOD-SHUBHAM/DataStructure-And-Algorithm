# Time and space = O(h) || O(n)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	# if nodetwo is a descendant of nodeone then check if nodethree is decendant of nodetwo
    if isDescendant(nodeTwo,nodeOne):
		return isDescendant(nodeThree,nodeTwo)
	
	# or
	
	# if nodetwo is a descendant of nodethree then check if nodeOne is decendant of nodetwo
    if isDescendant(nodeTwo,nodeThree):
		return isDescendant(nodeOne,nodeTwo)
    
	return False

def isDescendant(child,parent):
	if not parent:
		return False
	
	if child == parent:
		return True
	
	if child.value < parent.value:
		return isDescendant(child,parent.left)
	else:
		return isDescendant(child,parent.right)