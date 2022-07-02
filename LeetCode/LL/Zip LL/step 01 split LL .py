'''
Eg: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                  slow              fast
				  
split at 4 or i can split at 5 both are same.
because 3 should anyways point to 4.

'''

slow = head
fast = head

while fast or fast.next is not None:
    slow = slow.next
    fast = fasat.next.next
