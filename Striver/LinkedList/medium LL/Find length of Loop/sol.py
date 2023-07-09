# Tc: O(N) | Sc: O(1)

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    # Find the starting point
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # No cycle is found
    if not fast or not fast.next:
        return 0
    
    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    
    # print(slow.data)
    
    # Get the no of nodes in the cycle    
    slow = slow.next
    count = 1
    
    while slow != fast:
        count += 1
        slow = slow.next
    
    # print(count)
    
    return count