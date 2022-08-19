'''
Write a program to sort a stack such that smallest items are on the top. 
You can use an additional temporary stack, but you many not copy the elements to any other data structure.
The stack support following operation 
(push, pop, ppek, isempty).
'''

class SortStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def sortStack(self):
        while not self.isEmpty(self.s1):
            temp = self.pop(self.s1) # pop element from s1

            # s2 should not be empty and top of s2 
            # while not self.isEmpty(self.s2) and temp < self.peek(self.s2): this is for largest item on top
            while not self.isEmpty(self.s2) and temp > self.peek(self.s2): # this is for smallest item on top
                # pop the val from s2
                val = self.pop(self.s2)
                # push it to s1
                self.push(self.s1, val)

            # push the temp val to its right place
            self.push(self.s2 , temp)

    def push(self,stack ,x):
        # if s1 is empty
        if stack == "stack1":
            # then append to s1
            self.s1.append(x)
        else:
            stack.append(x)

    def pop(self, stack):
        if self.isEmpty(stack):
            print("stack underflow")
            exit(1)
        return stack.pop()

    def peek(self, stack):
        if self.isEmpty(stack):
            print("stack underflow")
            exit(1)
        return stack[-1]

    def isEmpty(self, stack):
        return len(stack) == 0

    def display(self):
        print(self.s2)

if __name__ == '__main__':
    stack = SortStack()
    stack.push("stack1", 34)
    stack.push("stack1", 3)
    stack.push("stack1" ,31)
    stack.push("stack1", 98)
    stack.push("stack1", 92)
    stack.push("stack1", 23)

    stack.sortStack()

    stack.display()




        
        


    