'''
Complexity Analysis

Time complexity: O(N). Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1) access later on.

Space complexity: O(N). The size of the stack in memory is proportional to N. Also, the memoization hash table is used, which occupies O(N) space.

'''

class Solution:
    cache = {0:0 , 1:1}
    
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.cache[n-1] + self.cache[n-2]

        return self.cache[n]
        