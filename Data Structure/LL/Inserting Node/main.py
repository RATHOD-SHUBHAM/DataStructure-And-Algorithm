class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert in beginning
    def beginning(self,new_val):
        new_node = Node(new_val)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # insert after a node
    def insertAfter(self,prev,new_val):
        new_node = Node(new_val)

        if prev is None:
            return

        new_node.next = prev.next
        prev.next = new_node
    
    # insert at end
    def end(self,new_val):
        new_node = Node(new_val)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    # traverse
    def printLL(self):
        point = self.head

        while point:
            print(point.val)
            point = point.next

if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(2)
    third = Node(3)
    four = Node(4)
    six = Node(6)

    ll.head.next = third
    third.next = four
    four.next = six

    ll.printLL()

    print("\n")

    ll.beginning(1)

    ll.insertAfter(four,5)

    ll.end(7)

    ll.printLL()