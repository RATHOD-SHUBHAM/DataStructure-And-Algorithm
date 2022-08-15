class stack:
    def __init__(self, k ,n):
        self.size = n # size of array
        self.k = k # stack size

        self.arr = [0] * self.size
        self.top = [-1] * self.k
        self.next = [i + 1 for i in range(self.size)]
        self.next[self.size - 1] = -1

        self.free = 0

    def isFull(self):
        if self.free == -1:
            return True
        else:
            return False

    def isEmpty(self, sn):
        if self.top[sn] == -1:
            return True
        else:
            return False

    def push(self, val, sn):

        if self.isFull():
            print("stack overflow")
            exit(1)

        # step 1: Update the free pointer
        idxToappend = self.free
        self.free = self.next[idxToappend]

        # step 2: insert value in array
        self.arr[idxToappend] = val

        # update next to point to previous value
        self.next[idxToappend] = self.top[sn]

        # update the top of stack
        self.top[sn] = idxToappend

    def pop(self,sn):

        if self.isEmpty(sn):
            print("stack underflow")
            exit(1)

        
        # get top of stack
        topOfstack = self.top[sn]

        # update top of stack to previous element
        self.top[sn] = self.next[topOfstack]

        # update next to point to previous
        self.next[topOfstack] = self.free

        self.free = topOfstack

        return self.arr[topOfstack]

    def display(self, sn):
        topOfstack = self.top[sn]

        while (topOfstack != -1):
            print(self.arr[topOfstack])
            topOfstack = self.next[topOfstack]


if __name__ == "__main__":
      
    # Create 3 stacks using an 
    # array of size 10.
    kstacks = stack(3, 10)
  
    # Push some items onto stack number 2.
    kstacks.push(15, 2)
    kstacks.push(45, 2)
  
    # Push some items onto stack number 1.
    kstacks.push(17, 1)
    kstacks.push(49, 1)
    kstacks.push(39, 1)
  
    # Push some items onto stack number 0.
    kstacks.push(11, 0)
    kstacks.push(9, 0)
    kstacks.push(7, 0)
  
    print("Popped element from stack 2 is " + 
                         str(kstacks.pop(2)))
    print("Popped element from stack 1 is " + 
                         str(kstacks.pop(1)))
    print("Popped element from stack 0 is " + 
                         str(kstacks.pop(0)))
  
    kstacks.display(0)


    