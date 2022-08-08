class LL:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,val):
        # check if this is the first element to be pushed in
        if self.head is None:
            self.head = LL(val)
        else:
            newNode = LL(val)
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        # check if there are any elements in stack
        if self.isEmpty():
            return None
        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.val

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.val

    def display(self):
        if self.isEmpty():
            return None
        else:
            curNode = self.head
            while curNode:
                print(curNode.val)
                curNode = curNode.next
            


if __name__ == '__main__':
    MyStack = Stack()
    MyStack.push(11) 
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
    
    # Display stack elements 
    print("display the stack elements")
    MyStack.display()
    
    # Print top element of stack 
    print("\nTop element is ",MyStack.peek())
    
    # Delete top elements of stack 
    print("Popped Node is: ",MyStack.pop())
    print("Popped Node is: ",MyStack.pop())
    
    # Display stack elements
    print("display the stack elements")
    MyStack.display()
    
    # Print top element of stack 
    print("\nTop element is ", MyStack.peek()) 