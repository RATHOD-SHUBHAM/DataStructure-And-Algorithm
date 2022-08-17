from collections import deque

class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Tc , Sc : O(n)
    # push the data in empty queue and then load the other queue data on top
    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())# remove from left and add on top

        self.q1 , self.q2 = self.q2 , self.q1

    # Tc,  Sc : O(1)
    def pop(self):
        # in stack we need to remove top element
        if self.q1:
            return self.q1.popleft()

    # Tc,  Sc : O(1)
    def top(self):
        if self.q1:
            return self.q1[0]

    # Tc,  Sc : O(1)
    def size(self):
        return len(self.q1)


# Driver Code
if __name__ == '__main__':
    s = stack()
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