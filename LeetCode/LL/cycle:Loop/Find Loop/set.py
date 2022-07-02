# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    hash = set()
	node = head
	
	# O(n) space O(n)
	# even if the value repeats we are not wooried because each node is unique
	# we are only worried when the node repeats
	while node:
		if node in hash:
			break
		hash.add(node)
		node = node.next
			
	return node
