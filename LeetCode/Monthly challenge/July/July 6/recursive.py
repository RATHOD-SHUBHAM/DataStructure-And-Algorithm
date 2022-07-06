'''
Complexity Analysis

Time complexity: O(2^N). This is the slowest way to solve the Fibonacci Sequence because it takes exponential time. The amount of operations needed, for each level of recursion, grows exponentially as the depth approaches N.

Space complexity: O(N). We need space proportional to N to account for the max size of the stack, in memory. This stack keeps track of the function calls to fib(N). This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a StackOverflowError. 

'''

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)