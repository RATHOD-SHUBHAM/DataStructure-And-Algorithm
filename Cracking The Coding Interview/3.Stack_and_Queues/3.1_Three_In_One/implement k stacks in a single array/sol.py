'''

Next array: 
1] says the next free spot in original array.
2] Says the previous stack elemnts index in array.


imagine a stack. The next element is actually the previous element.

4 steps in push operation:
  1. Update the current free spot.
  2. Insert item into the array.
  3. Update the next array.
  4. Update top of the stack.

5 steps in pop operation:
  1. Get the top of the stack.
  2. Update the top of the stack.
  3. Update the next array.
  4. Update the current free spot.
  5. Return the poped value from array.



'''
# Tc: O(1) for push and pop.
# Tc: O(n) as we are looping to print the stack.

# Sc : O(1)
# Sc: O(n) if we consider the array we are building.


class KStacks:
    def __init__(self, k, n):
        self.stack_size = k
        self.arr_size = n

        # initialize the array
        self.arr = [0] * self.arr_size

        # keep track of top of stack
        self.top = [-1] * self.stack_size

        # keep track of the next free spot in the array
        # as well as the previous element in stack
        self.next = [i+1 for i in range(self.arr_size)]
        self.next[self.arr_size - 1] = -1 # mark the last cell as -1 stating that there is no free space available after this.

        # keep track of cur free spot in array
        self.cur_free = 0


    def isFull(self):
        return self.cur_free == -1

    def isEmpty(self,stack_num):
        return self.top[stack_num] == -1 # if top is -1, then stack is empty

    def push(self, item, stack_num):
        if self.isFull():
            print("stack Overflow")
            exit(1)

        # step 1: Update the cur_free pointer
        insert_at_idx = self.cur_free
        self.cur_free = self.next[insert_at_idx] # get the next free spot in the array

        # step 2: Insert the Item into array
        self.arr[insert_at_idx] = item

        # step 3: Update the next array to point to next element in stack 
        self.next[insert_at_idx] = self.top[stack_num] # this will point to previous ele in stack.

        # step 4: Update the top of stack
        self.top[stack_num] = insert_at_idx # top of the stack will now have the idx of element that was just added to array.

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            print("stack underflow")
            exit(1)

        # step 1: Get the top of stack
        top_idx = self.top[stack_num]

        # step 2: Update the top of stack
        self.top[stack_num] = self.next[top_idx] # this will point to previous ele in stack which will be current top.

        # step 3: Update the next array
        self.next[top_idx] = self.cur_free # this will point to next free spot in array.

        # step 4: Update the cur_free pointer
        self.cur_free = top_idx # this idx is currently free now.

        # step 5: Return the item that was just popped
        return self.arr[top_idx]


    def printstack(self, stack_num):
        top_of_stack_idx = self.top[stack_num]

        while top_of_stack_idx != -1:
            print(self.arr[top_of_stack_idx])
            # get the previous element in stack
            top_of_stack_idx = self.next[top_of_stack_idx]


# Driver Code
if __name__ == "__main__":
      
    # Create 3 stacks using an 
    # array of size 10.
    kstacks = KStacks(3, 10)
  
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
  
    kstacks.printstack(0)