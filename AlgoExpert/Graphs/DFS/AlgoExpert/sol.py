# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
	
	# only write code here
	# Time = O(V+E)
	# Space = O(v)
    def depthFirstSearch(self, array):
        # Write your code here.
        array.append(self.name)
		
        for child in self.children:
            child.depthFirstSearch(array)

        # if there is no child then return the array
        return array