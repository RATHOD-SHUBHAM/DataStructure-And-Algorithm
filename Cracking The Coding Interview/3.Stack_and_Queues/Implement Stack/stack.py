'''
STACK uses LIFO (Last In First Out) principle.

Operations:
1. push(x) - add an element x to the top of the stack
2. pop() - remove the top element from the stack
3. peek() - return the top element from the stack
4. isEmpty() - return true if the stack is empty
5. size() - return the number of elements in the stack

'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def min(self):
        return min(self.items)

    def max(self):
        return max(self.items)

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.min())
    print(stack.max())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())
    print(stack.size())
