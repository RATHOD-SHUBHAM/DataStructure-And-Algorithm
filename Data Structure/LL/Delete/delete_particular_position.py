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

    def deleteNodePosition(self,k):
        # k is the position where I have to delete the node

        curNode = self.head

        # check if we have to delete the head node
        if curNode != None and k == 0:
            self.head = curNode.next
            curNode = None
            return


        # if not head node
        for i in range(k+1):
            if curNode != None:
                prevNode = curNode
                curNode = curNode.next

            if curNode != None and i+1 == k:
                prevNode.next = curNode.next
                curNode = None
                return



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
    ll.deleteNodePosition(5)

    ll.printLL()
