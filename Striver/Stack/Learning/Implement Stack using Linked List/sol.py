class Node:
    def __init__(self, val:int) -> None:
        self.val = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, x:int) -> None:
        '''
            Insert at the front of the stack
        '''
        # New node
        new_node = Node(x)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> int:
        '''
            Remove from the front of the stack.
        '''
        if self.head == None:
            return -1
        
        temp = self.head
        val = self.head.val

        # move the head pointers
        self.head = self.head.next

        # del the node
        del temp

        return val


    def peek(self) -> int:
        # Check if the LL is not empty
        if self.isEmpty():
            return -1
        
        top = self.head.val

        return top

    def display(self) -> None:
        # Check if the LL is not empty
        if self.isEmpty():
            return -1
        
        ptr = self.head

        while ptr:
            print(ptr.val)
            ptr = ptr.next


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False



if __name__ == '__main__':
    # Creating a stack
    st = Stack()

    # Push elements onto the stack
    st.push(95)
    st.push(87)
    st.push(0)
    st.push(4)
    st.push(5)

    # Print the stack
    st.display()

    # Print top element of the stack
    print("Top element is", st.peek())

    # removing two elemements from the top
    print("Removing two elements...");
    st.pop()
    st.pop()

    st.display()

    # Print top element of the stack
    print("Top element is", st.peek())