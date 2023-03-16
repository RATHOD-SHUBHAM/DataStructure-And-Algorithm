class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        curNode = self.head
        while curNode:
            print(curNode.value)
            curNode = curNode.next
            
    # deletes the entire linked list
    def deleteLL(self):
        self.head = None


if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    six = Node(6)

    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = six

    ll.printLL()
    print("\n")

    # delete the entire LinkedList
    ll.deleteLL()

    ll.printLL()
