class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        while self.head:
            print(self.head.val)
            self.head = self.head.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third  = Node(3)
    fourth = Node(4)

    ll.head.next = second
    second.next = third
    third.next = fourth


    ll.traverse()