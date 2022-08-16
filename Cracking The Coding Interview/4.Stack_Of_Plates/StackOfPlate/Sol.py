'''
Imagine a (literal) stack of plates. 
If the stack gets too high, it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
Implement a data structure SetOfStacks that mimics this. 
SetOfStacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. 
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

Input: capacity = 4 , push(1),push(2),push(2),pop,push(3),push(4),push(5)

Output: [[1,2,3,4],[5]]

'''

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity

        if self.capacity < 1:
            print("raising exception")

        self.stacks = [[]] # set of several stack
        # print(len(self.stacks))

    def push(self, val):
        len_of_stack = len(self.stacks[-1])

        # create new stack if exceed the limit
        if len_of_stack >= self.capacity:
            self.stacks.append([])


        self.stacks[-1].append(val)

    def pop(self):
        # check if the stacks has some stack in it
        if len(self.stacks) == 0:
            print("stack underflow")
            exit(1)
        else:
            val = self.stacks[-1].pop()
            # after poping check if the stack became empty
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            return val

    def display(self):
        print(self.stacks)

if __name__ == '__main__':
    sos = SetOfStacks(4)
    sos.push(1)
    sos.push(2)
    sos.push(3)
    sos.push(4)
    sos.push(5)
    sos.push(6)
    print(sos.pop())
    print(sos.pop())
    print(sos.pop())
    sos.push(7)
    sos.push(8)
    sos.push(9)
    sos.display()

