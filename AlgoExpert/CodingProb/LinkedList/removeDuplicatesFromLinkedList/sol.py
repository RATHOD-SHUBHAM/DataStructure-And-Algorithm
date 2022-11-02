# This is an input class. Do not edit.
# TC: O(n)
# Sc: O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None # default value added in end


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	# 1->2->1->1->3  : 1 = current node 2 = nextnode
	currentNode = linkedList #set first node to currrentNode
    while currentNode is not None:
		# if i have a current node set the next node
		nextNode = currentNode.next
		# if i use a if condition --> ill be deleting one node at one time
		# what is linked list was 1->1->1->1->3->4->5
		# to remove all the duplicate at once we will use a while loop
		while nextNode is not None and currentNode.value == nextNode.value:
			nextNode = nextNode.next
		
		# once i have removed my duplicate value
		# 1->3->4->5
		# my current node should point to 3
		currentNode.next = nextNode
		# then change my current node to 3
		currentNode = nextNode
	return linkedList
			
