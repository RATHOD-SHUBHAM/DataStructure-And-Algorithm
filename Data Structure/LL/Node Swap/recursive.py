# time = O(n)
# space = O(n)

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if head is None or head.next is None:
		return head
	
	curNode = head
	nextNode = curNode.next
	curNode.next = nodeSwap(nextNode.next)
	nextNode.next = curNode
	
	return nextNode