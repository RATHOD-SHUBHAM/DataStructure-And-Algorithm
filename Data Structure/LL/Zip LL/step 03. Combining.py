p1 = LinkedList1
p2 = LinkedList2

while p1 and p2:
    p3 = p1.next
    p4 = p2.next

    p1.next = p2
    p2.next = p3

    p1 = p3
    p2 = p4