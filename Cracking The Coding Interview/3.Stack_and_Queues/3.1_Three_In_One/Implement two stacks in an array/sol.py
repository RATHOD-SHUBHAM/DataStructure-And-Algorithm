# treat one array as 2 stack and push and pop element accordingly

# Tc: O(1)
# Sc: O(N) , Use of array to implement stack so it is a space-optimized method
# Sc: O(1), if array is not considered.

class twoStack:
    def __init__(self, length):
        self.length = length #size of array
        self.arr = [None] * self.length
        # stack one will fill from left to right
        self.top1 = -1 # top position for stack one
        # stack two will fill from right to left
        self.top2 = self.length

    def push1(self,num):
        # check if there is space between top1 and top2
        # -1 will check for 1 space. If it becomes equal then there is no space
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = num
        else:
            print("stack overflow")
            exit(1)

    def push2(self, num):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = num
        else:
            print("stack overflow")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            num = self.arr[self.top1]
            self.top1 -= 1
            return num
        else:
            print("stack underflow")
            exit(1)
    
    def pop2(self):
        if self.top2 < self.length:
            num = self.arr[self.top2]
            self.top2 += 1
            return num
        else:
            print("stack underflow")
            exit(1)

if __name__ == '__main__':
    toStack = twoStack(5) # 5 is the length of array
    toStack.push1(1)
    toStack.push2(5)
    toStack.push1(2)
    toStack.push2(6)
    toStack.push1(3)

    print("poped ele from stack1: ", toStack.pop1())
    toStack.push2(7)
    print('poped ele from stack2: ', toStack.pop2())