'''
Complexity Analysis

Time complexity: O(log N). We do not use loops or recursion, so the time required equals the time spent performing the calculation using Binet's formula. However, raising the golden_ratio to the power of NN requires O(log N) time.

Space complexity: O(1). The space used is the space needed to create the variable to store the golden ratio.

'''

class Solution:
    def fib(self, n: int) -> int:
        GR = (1 + (5 ** 0.5)) / 2
        return int(round( (GR **n) / (5 ** 0.5) ) )
        