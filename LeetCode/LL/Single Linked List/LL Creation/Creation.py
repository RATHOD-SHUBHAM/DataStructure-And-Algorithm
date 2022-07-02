'''
Representation: 

A linked list is represented by a pointer to the first node of the linked list. 
The first node is called the head. 
If the linked list is empty, then the value of the head is NULL. 

Each node in a list consists of at least two parts: 
1) data 
2) Pointer (Or Reference) to the next node 

'''

# Creation of a linked list

# Step 1: Create a class Node:
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# step 2: Create a class LinkedList:
class LinkedList:
    def __init__(self):
        self.head = None

# Step 3: Create a main function
if __name__== '__main__':
    # create a empty linked list
    LL = LinkedList()

    # add a head node to linked list
    LL.head = Node(1)

    # Create some node to append to liked list
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Attach the remaining nodes to head of Linked List
    LL.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth