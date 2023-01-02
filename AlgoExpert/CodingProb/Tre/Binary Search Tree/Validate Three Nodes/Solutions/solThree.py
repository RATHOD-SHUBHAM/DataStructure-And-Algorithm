# Time and Space = O(d), where d is the distance between nodeone and nodethree
# space = O(1)
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

'''
Start searching for nodetwo from both nodeone and nodethree
if anyone found nodethree. Then look for the althernate node from nodetwo.

While searching there are 4 edge cases:
1] nodeone met nodethree before meeting nodetwo
2] nodethree met nodeone before meeting nodetwo
3] Either one of the node met nodetwo
4] nodeone and nodethree reached end of the tree even before meeting nodetwo

'''
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
	# these value will keep getting updated
	node_one = nodeOne
	node_three = nodeThree
	
	while True:
		# case 1 and 2
		nodeOne_met_nodeThree = node_one is nodeThree
		nodeThree_met_nodeOne = node_three is nodeOne
		
		# case 3
		nodeTwo_found = node_one is nodeTwo or node_three is nodeTwo
		
		# case 4
		end_of_tree = node_one is None and node_three is None
		
		if nodeOne_met_nodeThree or nodeThree_met_nodeOne or nodeTwo_found or end_of_tree:
			break
		
		if node_one:
			node_one = node_one.left if nodeTwo.value < node_one.value else node_one.right
		
		if node_three:
			node_three = node_three.left if nodeTwo.value < node_three.value else node_three.right
	
	# case 1 and 2
	nodeOne_met_nodeThree = node_one is nodeThree
	nodeThree_met_nodeOne = node_three is nodeOne

	# case 3
	nodeTwo_found = node_one is nodeTwo or node_three is nodeTwo

	# case 4
	end_of_tree = node_one is None and node_three is None
	
	if nodeOne_met_nodeThree or nodeThree_met_nodeOne or not nodeTwo_found or end_of_tree:
			return False
		
	# else one of the node matched with node two
	
	if node_one is nodeTwo:
		return isDescendant(nodeThree,nodeTwo)
	else:
		return isDescendant(nodeOne,nodeTwo)
	
def isDescendant(child,parent):
	while parent and parent.value != child.value:
		if child.value < parent.value:
			parent = parent.left
		else:
			parent = parent.right
			
	if not parent or parent.value != child.value:
		return False
	else:
		return True