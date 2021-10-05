# Python3 program to partition a
# linked list around a given value.

# todo ---------- creating linked list --------------
# Link list Node
class Node:
    def __init__(self):
        self.data = 0
        self.next = None


# A utility function to create a new node
def newNode(data):
    new_node = Node()
    new_node.data = data
    new_node.next = None
    return new_node


# todo ------------- main logic --------------------
# Function to make two separate lists and return
# head after concatinating
def partition(head, x):
    node = head

    if node.next is None:
        return head

    # creating 4 pointers

    # smaller pointer to keep track of lest than x value
    # i need a head and tail so as to keep track of my first and last ele
    smallHead = smallTail= None

    # larger pointer to keep track of ele greater than x
    # i need a head and tail so as to keep track of my first and last ele
    largeHead = largeTail = None

    while node is not None:
        # check if the node is smaller than x
        if node.data < x:
            if smallHead == None:
                smallTail = smallHead = node
            else:
                # if i use head here and move my head to next element. i loose my linkedlist
                # because every time i more forward i loose track of prev element
                # and my linked list start from head
                smallTail.next = node
                smallTail = smallTail.next
        else:
            if largeHead == None:
                largeTail = largeHead = node
            else:
                largeTail.next = node
                largeTail = largeTail.next
        node = node.next

    # find last element and add null to next one
    if largeTail is not None:
        largeTail.next = None

    if smallHead == None:
        return largeHead

    smallTail.next = largeHead

    return smallHead


# ---------- printing linked list -------------------
# Function to print linked list
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next


# Driver code
if __name__ == '__main__':
    # create LinkedList
    head = newNode(3)
    head.next = newNode(5)
    head.next.next = newNode(8)
    head.next.next.next = newNode(5)
    head.next.next.next.next = newNode(10)
    head.next.next.next.next.next = newNode(2)
    head.next.next.next.next.next.next = newNode(1)
    print("the Linked List is: ")
    printList(head)
    print("\n")
    x = 5
    # call partiton
    head = partition(head, x)
    # call print
    print("linked List after partition")
    printList(head)
