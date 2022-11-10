"""
Steps: 
	1. Split the linkedList.
	2. Reverse the second half of LL.
	3. Combine the LinkedList

Eg: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                  slow              fast
				  
split at 4 or i can split at 5 both are same.
because 3 should anyways point to 4.

now 
reverse 
   5 -> 6
to 
   6 -> 5
   

"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    # Write your code here.
    # split the LinkedList
	slow = linkedList
	fast = linkedList
	
	while fast is not None and fast.next is not None:
		slow = slow.next
		fast = fast.next.next
		
	reversedLL = reversedLinkedList(slow.next)
	
	# make the first linkedlist point to none after they have split
	slow.next = None
	
	p1 = linkedList
	p2 = reversedLL
	
	while p2 is not None:
		p3 = p1.next
		p1.next = p2
		p4 = p2.next
		p2.next = p3
		p1 = p3
		p2 = p4
		
	return linkedList
	
	return head

def reversedLinkedList(head):
	prev, node = None, head
	
	while node is not None:
		next = node.next
		node.next = prev
		prev = node
		node = next
		
	return prev