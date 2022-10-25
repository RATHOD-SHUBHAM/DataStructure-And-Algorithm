class SortStack:
    def __init__(self):
        self.stack = []
        self.tempStack = []

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
        else:
            while self.stack and val > self.stack[-1]:
                self.tempStack.append(self.stack.pop())

            self.stack.append(val)

            while self.tempStack:
                self.stack.append(self.tempStack.pop())
            
    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

if __name__ == '__main__':
    stack = SortStack()
    stack.push(34)
    stack.push(3)
    stack.push(31)
    stack.push(98)
    stack.push(92)
    stack.push(23)

    stack.display()

    stack.pop()
    stack.display()

    stack.push(12)
    stack.push(120)
    stack.push(19)
    stack.push(1)

    print(stack.peek())

    stack.push(26)

    print(stack.isEmpty())

    stack.display()
    