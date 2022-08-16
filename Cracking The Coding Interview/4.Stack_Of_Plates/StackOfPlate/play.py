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
