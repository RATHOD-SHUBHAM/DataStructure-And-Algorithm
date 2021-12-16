# time = O(n)
# space = O(1)
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    if head is None or head.next is None:
		return head
	
	temp = LinkedList(0)
	temp.next = head
	prevNode = temp
	
	curNode = head
	
	while curNode and curNode.next:
		nextNode = curNode.next
		curNode.next = nextNode.next
		nextNode.next = curNode
		prevNode.next = nextNode
		
		prevNode = curNode
		curNode = curNode.next
		
	return temp.next

		
