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

# O(n) time and space O(1)
def findLoop(head):
    # Write your code here.
	'''
	first = second = head
	while head != second:
		# would terminate the loop in the first go
	'''
	# second will travell at a pase 2X
	first = head.next
	second = head.next.next
	
	while first != second:
		#find out a place where they cross paths
		first = first.next
		second = second.next.next
		
	# once they collide bring any of the pointer back to head
	first = head
	
	# check when first pointer and second pointer collide
	while first != second:
		first = first.next
		second = second.next
		
	# when they collide return any of the node
	return first
	
    
