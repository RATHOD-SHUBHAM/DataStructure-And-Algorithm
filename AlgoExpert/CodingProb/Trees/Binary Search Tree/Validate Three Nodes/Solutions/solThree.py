# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    node_one = nodeOne
    node_three = nodeThree

    # check if nodeOne is ancestor of nodeTwo or nodeThree is ancestor of nodeTwo
    while True:
        # nodeOne is ancestor of nodeTwo
        nodeOne_met_nodeThree = node_one is nodeThree
        # nodeThree is ancestor of nodeTwo
        nodeThree_met_nodeOne = nodeThree is nodeOne

        # check if both reached the end
        end_of_nodes = node_one is None and node_three is None

        if nodeOne_met_nodeThree or nodeThree_met_nodeOne or end_of_nodes:
            return False

        # check if nodeTwo was found
        node_two_found = node_one is nodeTwo or node_three is nodeTwo
        if node_two_found:
            break

        if node_one:
            if nodeTwo.value < node_one.value:
                node_one = node_one.left
            else:
                node_one = node_one.right
		
		if node_three:
			if nodeTwo.value < node_three.value:
                node_three = node_three.left 
            else:
                node_three = node_three.right
        

    # if nodeOne is ancestor of nodeTwo - Then check if Nodethree is decendant of nodeTwo
    if node_one is nodeTwo:
        return isDescendant(nodeThree , nodeTwo)
    else:
    # if Nodethree is ancestor of nodeTwo - Then check if nodeOne is decendant of nodeTwo
        return isDescendant(nodeOne, nodeTwo)

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