# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Tc and Sc : O(max(linkedListOne , linkedListTwo))
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    p = linkedListOne
	q = linkedListTwo
	carry = 0
	head = newList = LinkedList(0)
	
	while p or q or carry:
		cur_val = carry
		cur_val += 0 if p is None else p.value
		cur_val += 0 if q is None else q.value
		
		if  cur_val >= 10:
			carry = 1
			cur_val -= 10
		else:
			carry = 0
			
		newList.next = LinkedList(cur_val)
		newList = newList.next
		
		if p is None and q is None:
			break
		elif p is None:
			q = q.next
		elif q is None:
			p = p.next
		else:
			p = p.next
			q = q.next
			
	return head.next
		
