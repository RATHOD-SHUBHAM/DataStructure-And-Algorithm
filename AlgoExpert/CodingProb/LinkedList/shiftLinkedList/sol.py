# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) | O(1)
def shiftLinkedList(head, k):
	# since it is a rotation. After certain number of roatation my LL will 
	# look same as the initial linked list
	
	# abs(k) % len(ll)
	
	# calculate len of ll
	lastNode = head
	# base case
	if lastNode is None:
		return head
	
	LengthLL = 1 # linkedlist length
	
	# this will calculate the length of LL and lastNode will be at the very end
    while lastNode.next:
		lastNode = lastNode.next
		LengthLL += 1
		
	# check when the repeation occur
	# abs(k)  because k can be negative
	offSet = abs(k) % LengthLL
	
	# if offset == 0 then my linked list will be same as original ll after certain roatation
	if offSet == 0:
		return head
	
	# if k is positive remove node from back and put front
	# if k is negative -- remove node from front and put back
	if k > 0:
		pos = LengthLL - offSet
	else:
		pos = offSet
	
	
	node = head

    # point to one position before k
	for _ in range(pos - 1):
		node = node.next
	
	# change the pointers
    lastNode.next = head
	head = node.next
	node.next = None
	
	return head
		