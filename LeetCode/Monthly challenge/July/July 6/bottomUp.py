'''
Complexity Analysis

Time complexity: O(N). Each value from 2 to N is computed once. Thus, the time it takes to find the answer is directly proportional to N where N is the Fibonacci Number we are looking to compute.

Space complexity: O(1). This requires 1 unit of space for the integer N and 3 units of space to store the computed values (current, prev1, and prev2) for every loop iteration. The amount of space used is independent of NN, so this approach uses a constant amount of space.

'''

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        p_prev = 0
        prev = 1
        current = 0
        
        
        for i in range(2 , n + 1):
            current = p_prev + prev
            p_prev = prev
            prev = current
            
        return current