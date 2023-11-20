# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    # check if they reached the end
    if not fast or not fast.next:
        return None
    
    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow