# class to create list node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return True if self.head == None else False

    def push(self, val):
        if self.isEmpty():
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            nodeTopop = self.head
            self.head = self.head.next
            nodeTopop.next = None
            return nodeTopop

    def peek(self):
        return self.head.val
    
    def display(self):
        if self.isEmpty():
            return
        else:
            curNode = self.head
            while curNode:
                print(curNode.val)
                curNode = curNode.next


if __name__ == '__main__':
    MyStack = stack()
  
    MyStack.push(11) 
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
    
    # Display stack elements 
    MyStack.display()
    
    # Print top element of stack 
    print("\nTop element is ",MyStack.peek())
    
    # Delete top elements of stack 
    MyStack.pop()
    MyStack.pop()
    
    # Display stack elements
    MyStack.display()
    
    # Print top element of stack 
    print("\nTop element is ", MyStack.peek()) 
  
