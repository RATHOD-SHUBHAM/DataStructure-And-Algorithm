# ------------------ Two Stack ------------------

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # add to the min stack if needed
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()

        # Also make to remove from the minStack if it is present
        if val == self.minStack[-1]:
            min_val = self.minStack.pop()
        

    def top(self) -> int:
        top_val = self.stack[-1]
        return top_val
        

    def getMin(self) -> int:
        min_val = self.minStack[-1]
        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# ------------------ One Stack ------------------

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minVal = val
        else:
            cur_min = self.getMin()
            minVal = min(val, cur_min)

        self.stack.append((val, minVal))



    def pop(self) -> None:        
        val = self.stack.pop()


    def top(self) -> int:
        top_ele, _ = self.stack[-1]

        return top_ele
        

    def getMin(self) -> int:
        _, min_val = self.stack[-1]

        return min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()