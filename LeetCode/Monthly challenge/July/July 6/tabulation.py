'''
Complexity Analysis

Time complexity: O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.

Space complexity: O(N). The size of the data structure is proportional to N.

'''

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        # create table and intialize for number 0 and 1
        table = [0] * (n+1)
        table[1] = 1
        
        for i in range(2 , n+1):
            table[i] = table[i-1] + table[i-2]
            
        return table[n]