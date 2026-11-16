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
