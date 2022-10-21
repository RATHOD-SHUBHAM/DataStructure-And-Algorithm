# Tc: O(log N)
# sc :O(N)

from sortedcontainers import SortedList
class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = SortedList()
        self.cnt = 0

    def push(self, x: int) -> None:
        self.stack.append([self.cnt , x])
        # sort based on val
        self.maxStack.add((x , self.cnt))
        self.cnt += 1
        # print(self.maxStack)
        

    def pop(self) -> int:
        idx , val = self.stack.pop()
        self.maxStack.remove((val, idx))
        return val

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.maxStack[-1][0]

    def popMax(self) -> int:
        val , idx = self.maxStack.pop()
        self.stack.remove([idx, val])
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()