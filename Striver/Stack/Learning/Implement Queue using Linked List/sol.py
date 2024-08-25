class Node:
    def __init__(self, val:int) -> None:
        self.val = val
        self.next = None

    
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def enque(self, x:int) -> None:
        '''
            Append at the end of the LL
        '''
        new_node = Node(x)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def deque(self) -> int:
        '''
            Remove from the front of LinkedList
        '''

        if self.isEmpty():
            return -1
        
        val = self.head.val
        temp = self.head

        self.head = self.head.next

        # Check if this was the last node
        if self.head is None:
            self.tail = None

        del temp

        return val

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        
        top_ele = self.head.val

        return top_ele

    def display(self) -> None:
        if self.isEmpty():
            return -1

        ptr = self.head

        while ptr:
            print(ptr.val)
            ptr = ptr.next

    def isEmpty(self) -> bool:
        if self.head is None and self.tail is None:
            return True
        else:
            return False
        

if __name__ == '__main__':
    # Creating a stack
    q = Queue()

    # Push elements onto the stack
    q.enque(95)
    q.enque(87)
    q.enque(0)
    q.enque(4)
    q.enque(5)

    # Print the stack
    q.display()

    # Print top element of the stack
    print("Top element is", q.peek())

    # removing two elemements from the top
    print("Removing two elements...");
    q.deque()
    q.deque()

    q.display()

    # Print top element of the stack
    print("Top element is", q.peek())