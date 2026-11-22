# 1. ============================================  704. Binary Search ============================================================================
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

# ============================================ Bisect Left ============================================================================
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        idx = bisect.bisect_left(nums, target)

        # bounds guard
        if idx >= len(nums):
            return -1

        if nums[idx] == target: # nums[i] >= t
            return idx
        else:
            return -1

# ============================================ Bisect Right ============================================================================
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        idx = bisect.bisect_right(nums, target)

        # bounds guard
        if idx - 1 < 0:
            return -1

        if nums[idx-1] == target: # nums[i] > t
            return idx - 1
        else:
            return -1

# 2. ============================================ 35. Search Insert Position ============================================================================
class Solution:
    def bisect_left(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
            
        return left
    
    def bisect_right(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
            
        return left

    def searchInsert(self, nums: list[int], target: int) -> int:
        idx_left = self.bisect_left(nums, target)
        print(idx_left)

        idx_right = self.bisect_right(nums, target)
        print(idx_right)

        return idx_left # or idx_right

# ============================================ Combine 1 adn 2 ============================================================================
def bisect_left(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid          # keep mid as a candidate
    return left


def bisect_right(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:  # the only change: < becomes <=
            left = mid + 1
        else:
            right = mid
    return left


# LeetCode 35: works with or without duplicates
def searchInsert(nums, target):
    return bisect_left(nums, target)


# LeetCode 34: first and last occurrence
def searchRange(nums, target):
    first = bisect_left(nums, target)
    last = bisect_right(nums, target) - 1
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, last]


# 3. ============================================ 374. Guess Number Higher or Lower ============================================================================
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            pick = guess(mid) # call the api

            if pick == -1:
                right = mid - 1
            elif pick == 1:
                left = mid + 1
            else:
                return mid


# 4. ============================================ 69. Sqrt(x) ============================================================================
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


# 5. ============================================ 74. Search a 2D Matrix ============================================================================
class Solution:
    def findTarget(self, arr, n, target):
        left = 0
        right = n - 1

        while left <= right: 
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if self.findTarget(matrix[i], n, target) == True:
                return True
        
        return False

# =============================================== Search 2D Matrix  ===============================================

# Tc: O(log(m*n)) | Sc: O(1)
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Flatten the index
        left = 0
        right = (m*n) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Bring index back to 2D Space
            r = mid // n
            c = mid % n

            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

# 6. ============================================ 875. Koko Eating Bananas ============================================================================
# Tc: O(nlogm) | Sc: O(1)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n = len(piles)

        max_val = max(piles)

        left = 1
        right = max_val

        while left < right:
            mid = left + (right - left) // 2 # Rate at which koko will eat banana

            total_time_taken = 0
            for i in range(n):
                time_taken = math.ceil(piles[i] / mid)
                total_time_taken += time_taken


            if total_time_taken <= h:
                # Koko can comfortably finish in given time with this rate, so try to further lower the speed and check
                right = mid
            else:
                left = mid + 1 # increase the rate at which koko eats, so she can finish on time
        
        return left # or right

# 7. ============================================ 1011. Capacity To Ship Packages Within D Days ============================================================================
# Find the smallest capacity of ship such that all packages can be shipped within d days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights) # the ship has to be able to carry the heaviest single package, otherwise that package could never be shipped.
        right = sum(weights) # load all the package in one day, so ship weight should be sum of all weights

        while left < right:
            # pick a capacity to test if this can be taken in d days
            mid = left + (right - left) // 2 # weight of ship

            # Calculate how many days will it take with current weight of the ship
            no_of_days = 1 # Because the first day is already in progress before you load anything
            load = 0
            for w in weights:
                # If the load exceeds the ship weight, load it the next day
                if load + w > mid:
                    no_of_days += 1
                    load = w
                
                else:
                    load += w
            
            # Adjust the capacity
            if no_of_days <= days:
                # If the weight of ship is high such that we are taking less days than given days, we can try reducing the load of ship
                right = mid
            else:
                left = mid + 1
        
        return left