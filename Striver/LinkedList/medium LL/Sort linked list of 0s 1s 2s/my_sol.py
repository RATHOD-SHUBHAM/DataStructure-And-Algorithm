class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    # Write your code here
    cur = head

    # Create 3 individual LL
    dummy0 = pt0 = Node(-1)
    dummy1 = pt1 = Node(-1)
    dummy2 = pt2 = Node(-1)


    while cur:
        if cur.data == 0:
            pt0.next = cur
            cur = cur.next
            pt0 = pt0.next
            pt0.next = None
        elif cur.data == 1:
            pt1.next = cur
            cur = cur.next
            pt1 = pt1.next
            pt1.next = None
        else:
            pt2.next = cur
            cur = cur.next
            pt2 = pt2.next
            pt2.next = None

    # Merge the LL
    pt0.next = dummy1.next
    pt1.next = dummy2.next

    return dummy0.next