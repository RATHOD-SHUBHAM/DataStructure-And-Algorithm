# https://leetcode.com/problems/sqrtx/solutions/8617044/brute-force-binary-search-2-approach-opt-emxb

# ===================================== Brute Force =====================================
# The square root of x is the number that, multiplied by itself, gives x.
# k * k = x, in our case we have to round it down so k * k <= x
# O(√x) time. 

class Solution:
    def mySqrt(self, x: int) -> int:
        k = 0
        # Check if k hold number that works for k * k <= x
        while (k+1) * (k+1) <= x:
            k += 1
        
        return k


# Time: O(log x), about 31 iterations at most.
# Space: O(1).
# ===================================== k * k > x =====================================
# Find the first k where k*k > x

class Solution:
    def mySqrt(self, x: int) -> int:
        # Bisect right
        left = 0
        right = x + 1 # consider case where input x = 1

        while left < right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                left = mid + 1 # “mid is good, so the first bad one is after mid.”
            else:
                right = mid # mid is bad, so the first bad one is at mid or earlier.”
        
        #  Bisect right returns the first index where the value is strictly greater than the target, and the last valid element is one position before that
        return left - 1


# ===================================== k * k <= x =====================================
# Find the last good k, where k * <= x
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        ans = 0 # keep track of the answer

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                ans = mid # This can be a potential answer

                left = mid + 1
            else:
                right = mid - 1
            
        return ans

# ===================================== Optional Speedup =====================================
# Optional speedup: for x >= 2, the root is at most x // 2, so you can start with right = x // 2. It’s a constant-factor gain and not required.
# Find the last good k, where k * <= x
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x if x <=1 else x // 2

        ans = 0 # keep track of the answer

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                ans = mid # This can be a potential answer

                left = mid + 1
            else:
                right = mid - 1
            
        return ans


# ===================================== Newton’s method =====================================
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