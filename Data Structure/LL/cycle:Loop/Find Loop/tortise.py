'''
first pointer will cover distance of d + p when it interacts with second pointer

f = d + p -- eq 1

second pointer is moving 2x faster than first pointer

s = 2x(f) = 2 x (d+p) = 2d + 2p -- eq 2

total distance t = d + p + r  -- eq 3

which also means
second pointer s cover a distance of s = t + p  --  eq 4

there fore
t = s - p
substituting eq 2
t = 2d + 2p - p
t = 2d + p -- eq 5

Now appending eq 5 in eq 3
eq 3 => t = d + p + r
2d + p = d + p + r

ie d = r


'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
    first = head.next
	second = head.next.next
	
	while first != second:
		first = first.next
		second = second.next.next
	
	first = head
	
	while first != second:
		first = first.next
		second = second.next
		
	return first
