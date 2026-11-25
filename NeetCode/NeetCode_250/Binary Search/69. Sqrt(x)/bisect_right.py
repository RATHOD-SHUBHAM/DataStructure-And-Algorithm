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

# ========================== Bisect Right II ==========================

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1