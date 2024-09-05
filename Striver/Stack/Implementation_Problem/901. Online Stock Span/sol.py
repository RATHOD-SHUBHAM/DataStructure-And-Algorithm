# Tc: O(n) | Sc: O(1)

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1


        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        
        if not self.stack:
            op = self.idx + 1
        else:
            op = self.idx - self.stack[-1][1]

        self.stack.append((price, self.idx))


        return op


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)