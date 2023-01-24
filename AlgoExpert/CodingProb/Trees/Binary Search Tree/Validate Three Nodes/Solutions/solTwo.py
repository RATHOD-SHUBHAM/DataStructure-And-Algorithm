# time and space = O(h) || O(1)

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

def isDescendant(child, parent):
    while parent and child.value != parent.value:
        if child.value < parent.value:
            parent = parent.left
        else:
            parent = parent.right

    if not parent:
        return False
    else:
        return True
