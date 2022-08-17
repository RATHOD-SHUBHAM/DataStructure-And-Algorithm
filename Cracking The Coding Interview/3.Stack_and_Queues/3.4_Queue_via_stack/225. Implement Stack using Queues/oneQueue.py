from collections import deque

class stack:
    def __init__(self):
        self.q1 = deque()

    # Tc: O(n), Sc: O(n)
    def push(self, x):
        # get the curlen of queue
        curlen = len(self.q1)

        # append the value to the end
        self.q1.append(x)

        # take all the value previous end and append it one by one after last value
        for _ in range(curlen):
            self.q1.append(self.q1.popleft())

    # Tc: O(1), Sc: O(1)
    def pop(self):
        return self.q1.popleft()

    # Tc: O(1), Sc: O(1)
    def top(self):
        return self.q1[0]

    # Tc: O(1), Sc: O(1)
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