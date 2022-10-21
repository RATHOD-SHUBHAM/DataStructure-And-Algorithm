class stack:
    def __init__(self, k ,n):
        self.stackSize = k
        self.arrSize = n
        
        self.curFree = 0

        self.arr = [0] * self.arrSize
        self.top = [-1] * self.stackSize
        self.next = [i+1 for i in range(self.arrSize)]

    def isFull(self):
        return self.curFree == -1

    def isEmpty(self, stackNo):
        return self.top[stackNo] == -1

    def push(self, val, sn):
        if self.isFull():
            print("stack overFlow")
            exit(1)
        else:
            # step 1: update the curFree pointer
            index_to_insert = self.curFree
            self.curFree = self.next[index_to_insert]

            # step 2: insert the elemenet into array
            self.arr[index_to_insert] = val

            # step 3: update the next array to point to previous element in stack
            self.next[index_to_insert] = self.top[sn]
            
            # update the top of stack
            self.top[sn] = index_to_insert


    def pop(self,sn):
        if self.isEmpty(sn):
            print("stack underflow")
            exit(1)
        else:
            # step 1: get the top idx
            top_idx = self.top[sn]

            # step 2: update the top of stack
            self.top[sn] = self.next[top_idx]

            # step 3: update next arr
            self.next[top_idx] = self.curFree

            # step 4:  update curFree
            self.curFree = top_idx

            # step 5: return the popped array
            return self.arr[top_idx]


    def display(self, sn):
        # step 1: get the top idx
        top_idx = self.top[sn]

        while top_idx != -1:
            print(self.arr[top_idx])
            top_idx = self.next[top_idx]


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


    