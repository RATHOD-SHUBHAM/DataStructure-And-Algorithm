# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(headOne + headTwo) | O(1)
def mergeLinkedLists(headOne, headTwo):
    prev = dummy = LinkedList(-1)
    p = headOne
    q = headTwo

    while p and q:
        if p.value <= q.value:
            prev.next = p
            p = p.next
            prev = prev.next
        else:
            prev.next = q
            q = q.next
            prev = prev.next

    prev.next = p if p is not None else q

    return dummy.next
