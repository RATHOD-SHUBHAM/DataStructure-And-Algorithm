# Tc: O(m + n)
# Sc: O(1)

from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ncr formula
        N = m + n - 2
        
        return factorial(N) // factorial(m-1) // factorial(n-1)