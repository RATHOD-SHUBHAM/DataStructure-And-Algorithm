# todo: Creating Node

class Node:
    def __init__(self, data):
        # Assign data
        self.data = data
        # Initialize next as null
        self.next = None


# todo: Creating Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def decimalValue(self, head):
        # todo: type1
        # res = 0
        # while head:
        #     res = ( res << 1 )+head.data
        #     head = head.next
        # return res

        # todo: type 2
        # int("str",2)          # one method to convert binary to decimal
        res = ""
        while head:
            res += str(head.data)
            head = head.next
        return int(res, 2)


if __name__ == '__main__':
    # start with an empty linked list
    Llist = LinkedList()
    Llist.head = Node(1)
    Llist.head.next = Node(0)
    Llist.head.next.next = Node(1)
    Llist.head.next.next.next = Node(1)
    print("Decimal value is {}".format(Llist.decimalValue(Llist.head)))
