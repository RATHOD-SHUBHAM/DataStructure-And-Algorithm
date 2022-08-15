class DinnerPlate:
    def __init__(self,capacity):
        self.capacity = capacity
        self.heaps = []
        self.stacks = []

    def push(self, value):
        if self.heaps:
            idx = heapq.heappop() # get the idx of the stack where there is space
            # if idx is present in queue
            if idx < len(self.stacks):
                self.heap[idx].append(value)
            else:
                self.push(val) # if the given idx is not present
        elif self.stacks:
            if len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].append(value)
            else:
                self.stacks.append([])
                self.stacks[-1].append(value)
        else:
            self.stacks.append([])
            self.stacks[-1].append(value)

    def pop(self):
        # first check if the stacks has any stack
        while self.stacks:
            # I would have poped from idx and made stack empty but wouldnt have removed empty stack form stacks 
            # check if the last stack is empty. if empty remove it and return the new top of stack
            if len(self.stacks[-1]) == 0:
                self.stacks.pop()
            else:
                val = self.stacks[-1]
                # check if removing this makes the stack empty
                if len(self.stacks[-1]) == 0:
                    self.stacks.pop()

                return val

        return -1

    def popAtStack(self, index):
        # if the index is index of last stack
        if index == len(self.stacks) - 1:
            return self.pop() # pop from the last stack

        elif index < len(self.stacks) - 1:
            # get the stack at that particular index
            stack = self.stacks[index]
            # if stack is present
            if stack:
                val = stack.pop()
                heapq.heappush(self.heap , index)
                return val
            else:
                return -1
        else:
            return -1




