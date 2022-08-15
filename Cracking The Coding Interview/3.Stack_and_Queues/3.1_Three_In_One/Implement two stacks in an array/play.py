from xmlrpc.server import SimpleXMLRPCDispatcher


class stack:
    def __init__(self, size):
        self.n = size
        self.arr = [0] * self.n

        self.left = -1
        self.right = self.n

    def pushOne(self,val):
        # check if there is a free space only then insert
        if self.left < self.right - 1:
            self.left += 1
            self.arr[self.left] = val
        else:
            print("stack overflow")
            exit(1)

    def pushTwo(self, val):
        if self.left < self.right - 1:
            self.right -= 1
            self.arr[self.right] = val
        else:
            print("stack overflow")
            exit(1)

    def popOne(self):
        if self.left >= 0:
            valTopop = self.arr[self.left]
            self.left -= 1
            return valTopop
        else:
            print("stack underflow")
            exit(1)

    def popTwo(self):
        if self.right < self.n:
            valTopop = self.arr[self.right]
            self.right += 1
            return valTopop

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



