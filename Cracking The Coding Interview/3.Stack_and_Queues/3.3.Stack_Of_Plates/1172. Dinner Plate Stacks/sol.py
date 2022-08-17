class DinnerPlates:

    def __init__(self, capacity: int):
        self.heap = []
        self.stacks = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        # when there is a empty space in stack
        if self.heap:
            index = heapq.heappop(self.heap)
            if index < len(self.stacks):
                self.stacks[index].append(val)
            else:
                self.push(val)
        
        # adding 2 or more stack
        elif self.stacks:
            if len(self.stacks[-1]) < self.capacity:
                self.stacks[-1].append(val)
            else:
                self.stacks.append([])
                self.stacks[-1].append(val)
        
        # first element to be added in stack
        else:
            self.stacks.append([])
            self.stacks[-1].append(val)
            
    def pop(self) -> int:
        while self.stacks:
            lastStack = self.stacks[-1]
            if len(self.stacks[-1]) != 0:
                val = lastStack.pop()
                if len(self.stacks[-1]) == 0:
                    self.stacks.pop()
                return val
            # after pop at index i dont have to delete stack as there might be a push operation
            # but if after pop at index there is one more pop and if the stack is empty. 
            # well have to remove the stack from stack and then return top of the stack
            else:
                self.stacks.pop()
        return -1

    def popAtStack(self, index: int) -> int:
        # if the index is index of last stack
        if index == len(self.stacks) - 1:
            return self.pop()
        elif index < len(self.stacks) - 1:
            stack = self.stacks[index]
            if stack:
                val = stack.pop()
                heapq.heappush(self.heap, index)
                return val
            else:
                return -1
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)