class stack:
    def __init__(self, size):
        self.n = size
        self.arr = [None] * self.n
        self.top1 = -1
        self.top2 = self.n

    def pushOne(self,val):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.arr[self.top1] = val
        else:
            print("stack overflow")
            exit(1)

    def pushTwo(self, val):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = val
        else:
            print("stack overflow")
            exit(1)

    def popOne(self):
        if self.top1 >= 0:
            val = self.arr[self.top1]
            self.top1 -= 1
            return val
        else:
            print("list underflow")
            exit(1)

    def popTwo(self):
        if self.top2 < self.n:
            val = self.arr[self.top2]
            self.top2 += 1
            return val
        else:
            print("stack underflow")
            exit(1)

if __name__ == '__main__':
    ts = stack(5)
    ts.pushOne(5)
    ts.pushTwo(10)
    ts.pushTwo(15)
    ts.pushOne(11)
    ts.pushTwo(7)
    
    print("Popped element from stack1 is " + str(ts.popOne()))
    ts.pushTwo(40)
    print("Popped element from stack2 is " + str(ts.popTwo()))



