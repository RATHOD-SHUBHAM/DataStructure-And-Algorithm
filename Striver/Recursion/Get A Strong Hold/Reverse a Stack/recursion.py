# Tc: O(n^2) | Sc: O(1)

from typing import List

# Sum of N over all test cases doesn't exceeds 106
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def reverse(self,St): 
        if not St:
            return
        
        # Store the top element of the stack
        x = St.pop(0)

        # Call for the remaining stack
        self.reverse(St)
        
        St.append(x)