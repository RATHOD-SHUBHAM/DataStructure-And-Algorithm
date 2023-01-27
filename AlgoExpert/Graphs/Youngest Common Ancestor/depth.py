# Time = O(d) where d is the depth of the tree
# Space = O(1)

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # find the dept of both decendant
	dept_of_descendantOne = dept(descendantOne,topAncestor)
	dept_of_descendantTwo = dept(descendantTwo,topAncestor)
	
	if dept_of_descendantOne > dept_of_descendantTwo:
		diff = dept_of_descendantOne - dept_of_descendantTwo
		return findCommonAncestor(descendantOne,descendantTwo,diff)
	# if less than or equal to	
	else:
		diff = dept_of_descendantTwo - dept_of_descendantOne
		return findCommonAncestor(descendantTwo,descendantOne,diff)

def dept(node,topAncestor):
	depth = 0
	
	while node != topAncestor:
		depth += 1
		node = node.ancestor
	
	# when node has reached the top -- return depth
	return depth

def findCommonAncestor(lowerNode, upperNode, diff):
	while diff > 0:
		lowerNode = lowerNode.ancestor
		diff -= 1
	
	# now both node are on same level. check thier common ancestor
	while lowerNode != upperNode:
		lowerNode = lowerNode.ancestor
		upperNode = upperNode.ancestor
	
	return upperNode # can return any node as both will be pointing to same node