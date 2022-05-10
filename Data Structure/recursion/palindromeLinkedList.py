# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    # Write your code here.
    slow = head
	fast = head
	
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
		
	reverseLL = reverseLinkedList(slow)
	
	p1 = head
	p2 = reverseLL
	
	while p2 is not None:
		if p1.value != p2.value:
			return False
		p1 = p1.next
		p2 = p2.next
		
	return True

def reverseLinkedList(head):
	prev , node = None , head
	
	while node is not None:
		next = node.next
		node.next = prev
		prev = node
		node = next
	
	return prev
