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
        