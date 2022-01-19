# Time = O(V+E)
# Space = O(V)

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	
	# only add code here
    def breadthFirstSearch(self, array):
        q = [self]
		
		while q:
			curNode = q.pop(0) # pop left
			array.append(curNode.name)
			
			for child in curNode.children:
				q.append(child)
				
		return array