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

    def deleteNode(self,k):
        # k is the node to delete

        curNode = self.head

        # check if the node to delete is head node
        if curNode != None and curNode.value == k:
            self.head = curNode.next
            curNode = None
            return
        
        # if not the head node
        while curNode:
            if curNode.value == k:
                break
            prevNode = curNode
            curNode = curNode.next

        if curNode == None:
            return
        prevNode.next = curNode.next
        curNode = None



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

    # delete node 4
    ll.deleteNode(4)

    ll.printLL()
