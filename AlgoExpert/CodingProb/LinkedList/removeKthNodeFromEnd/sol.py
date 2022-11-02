# This is an input class. Do not edit.
# Do this question from leetcode
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Tc: O(n) | Sc : O(1)
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    left = right = head
	
	# this will create a window size of k between left and right
	for i in range(k):
		right = right.next
		
	if right == None:
		head.value = head.next.value
		head.next = head.next.next
		return head
	
	while right.next:
		left = left.next
		right = right.next
		
	left.next = left.next.next
	
	return head
