# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) | O(1)
def reverseLinkedList(head):
    # Write your code here.
    prev_node = None
	node = head
	
	while node:
		next_node = node.next
		node.next = prev_node
		prev_node = node
		node = next_node
		
	return prev_node
