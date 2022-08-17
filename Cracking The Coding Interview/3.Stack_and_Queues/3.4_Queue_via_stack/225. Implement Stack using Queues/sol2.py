from collections import deque
class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Tc,  Sc : O(1)
    def push(self,x):
        self.q1.append(x)

    # Tc , Sc : O(n)
    # move all the element except the last to empty cell and pop the last ele
    def pop(self):
        if not self.q1:
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # return the last element
        val = self.q1.popleft()

        # swap the cells
        self.q1, self.q2 = self.q2, self.q1

        return val
    
    # Tc,  Sc : O(1)
    def top(self):
        if not self.q1:
            return -1

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        top = self.q1[0]

        self.q2.append(self.q1.popleft())

        self.q1 , self.q2 = self.q2 , self.q1

        return top

    # Tc,  Sc : O(1)
    def size(self):
        return len(self.q1)




if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
 
    print("current size: ", s.size())
    print("The top value is: ",s.top())
    print("The poped value is : ",s.pop())
    print("The top value is : ",s.top())
    print("The poped value is : ",s.pop())
    print("The top value is: ",s.top())

    print("current size: ", s.size())