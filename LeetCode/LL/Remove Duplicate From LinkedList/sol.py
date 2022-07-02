# Because the nodes are in sorted order I only have to look at next node to check if there are duplicates.

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curNode = linkedList
	# will run for every ele till the end = O(n)
	while curNode is not None:
		# will not run till end
		while curNode.next is not None and curNode.value == curNode.next.value:
			curNode.next = curNode.next.next
		
		curNode = curNode.next
		
	return linkedList