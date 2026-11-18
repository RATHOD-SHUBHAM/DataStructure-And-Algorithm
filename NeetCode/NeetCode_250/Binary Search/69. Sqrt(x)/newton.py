# Good to know - not necessarily to remember for interview
"""
# The idea

Say you have a guess r that is too big (r * r > x). Then x // r is too small.

Why: r * (x / r) = x. If r is bigger than the true root, the other factor x / r has to be smaller than the true root. The two factors multiply to x, so one sits above the root and one sits below.

So the real root is trapped between x // r and r. Averaging them gives a better guess:
    new r = (r + x // r) // 2
Repeat until the guess is no longer too big (r * r <= x).

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x

        while r * r > x:
            r = (r + (x//r)) // 2
        
        return r