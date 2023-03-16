# Time = average - O(log n) | worst - O(n)
# space = O(1)

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		# Write your code here.
		# Do not edit the return statement of this method.
		curNode = self

		while True:
			if value < curNode.value:
				if not curNode.left:
					# if there is no element on left -- add the element to left
					curNode.left = BST(value) 
					break
				else:
					curNode = curNode.left
			else:
				if not curNode.right:
					curNode.right = BST(value)
					break
				else:
					curNode = curNode.right
					
		return self

    def contains(self, value):
        # Write your code here.
        curNode = self
		
		while curNode:
			if value < curNode.value:
				curNode = curNode.left
			elif value > curNode.value:
				curNode = curNode.right
			else:
				return True
		return False

    def remove(self, value, parentNode = None):
        # Write your code here.
        # Do not edit the return statement of this method.
		curNode = self
		
		while curNode:
			# step 1 = search
			if value < curNode.value:
				parentNode = curNode
				curNode = curNode.left
			elif value > curNode.value:
				parentNode = curNode
				curNode = curNode.right

			else: # value found to be deleted
				# case1 : when node has 2 child
				if curNode.left and curNode.right:
					# get the smallest value from right tree
					curNode.value = curNode.right.getMin()
					# delete the smallest node
					curNode.right.remove(curNode.value,curNode) # if there are only 2 node and i want to delete parent,
					# then there should be a way for me the replace the parent with child node and delete child.
					# tracking can be done using parent node as reference
					
				# case 2: when there is only one child
				# case a: when it has no parent
				else: # found the node to be deleted
                # check if the node has 2 node
                if curNode.left and curNode.right:
                    curNode.value = self.getMin(curNode.right)
                    curNode.right.remove(curNode.value, curNode)
                else: # there is only one node
                    if not parentNode:
                        if curNode.left:
							# here we change only the value
                            curNode.value = curNode.left.value
							# here we change the node
                            curNode.right = curNode.left.right
                            curNode.left = curNode.left.left
                        elif curNode.right:
                            curNode.value = curNode.right.value
                            curNode.left = curNode.right.left
                            curNode.right = curNode.right.right
                        else:
                            pass
                    else: # there is parent node
                        if parentNode.left == curNode:
                            parentNode.left = curNode.left if curNode.left else curNode.right
                        elif parentNode.right == curNode:
                            parentNode.right = curNode.right if curNode.right else curNode.left

                break 


    def getMin(self, root):
        node = root

        while node.left:
            node = node.left

        return node.value
