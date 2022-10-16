'''
Complexity Analysis

Given nn as the number of calls to next,

Time complexity of each call to next: O(1)

Even though there is a while loop in next, that while loop can only run n times total across the entire algorithm. Each element can only be popped off the stack once, and there are up to n elements.

This is called amortized analysis - if you average out the time it takes for next to run across nn calls, it works out to be O(1). If one call to next takes a long time because the while loop runs many times, then the other calls to next won't take as long because their while loops can't run as long.

Space complexity: O(n)

In the worst case scenario for space (when all the stock prices are decreasing), the while loop will never run, which means the stack grows to a size of nn.

'''


# tc: O(1)
# sc: O(n)

# Previous greater element
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            _ , prev_span = self.stack.pop()
            span += prev_span


        self.stack.append([price , span])
        return span
            
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)