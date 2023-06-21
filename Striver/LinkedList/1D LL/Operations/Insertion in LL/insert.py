class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at the beginning / Front of the LL
    def front(self, n):
        # create a new node
        new_node = Node(n)

        # Attach it to the head of LL
        if self.head != None:
            new_node.next = self.head

        # make new node as the head
        self.head = new_node

    # Insert after a given node
    def after(self, node, n):
        # check if the node exist
        if node is None:
            print("Node doesnot exist")
            return
        
        # create a new node
        new_node = Node(n)

        # make the newnodes next pointer point to nodes next pointer
        new_node.next = node.next

        # make the node point to new node
        node.next = new_node

    
    # Insert at the end of the LL
    def end(self, n):
        # create a new node
        new_node = Node(n)

        # check if the LL is empty
        if self.head == None:
            self.head = new_node
            return
        
        # Traverse to the end
        last = self.head
        while (last.next != None):
            last = last.next
        
        last.next = new_node

    # Display LL
    def display_LL(self):
        if self.head == None:
            print("Linked List is empty")
            return
        else:
            node = self.head

            while node:
                print(node.val, end = " ")
                node = node.next

    

if __name__ == '__main__':
    LL = LinkedList()

    arr = [1, 2, 3, 4, 5]

    for i in arr:
        LL.front(i)
    
    LL.end(6)
    
    LL.display_LL()
    