#User function Template for python3

from typing import List

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def reverse(self,St): 
        if not St:
            return
        
        x = St.pop(0)
        
        self.reverse(St)
        
        St.append(x)
        
        return St
