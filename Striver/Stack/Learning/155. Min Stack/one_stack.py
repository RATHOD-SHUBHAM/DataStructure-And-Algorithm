class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        '''
            Always store value and current min value of the stack in the stack
        '''
        if not self.stack:
            '''
            Initially or if at some point stack becomes empty then reset the minVal of the stack
            '''
            minVal = val
        else:
            '''
                Get the current minVal from the stack
            '''
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