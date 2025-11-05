# ----------------   Brute Force --------------------------------

# Tc :O(n^2) | Sc :O(n)

'''
    rotate the array every time and check if it is sorted
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)

        for i in range(n):
            new_nums = nums[i : ] + nums[ : i]

            if new_nums == sorted_nums:
                return True
        
        return False
    
# ------------------------- Better Brute: Inflation Point ----------------------------

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)

        inflation_point = 0

        for i in range(1, n):
            # Compare to previous element to get the inflation point
            if nums[i-1] > nums[i]:
                inflation_point = i
        
        new_nums = nums[inflation_point : ] + nums[ : inflation_point]

        return new_nums == sorted_nums
    

# ----------------------- Binary Search -----------------------------


'''
    We Know that when an array is sorted 
        right > left

    When the array is rotated
        - if mid > right:
            then left of mid is all smaller than mid and greater than left
        
        - if mid < right:
            then right side of mid is all greater than mid and less than right
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_nums = sorted(nums)

        left = 0
        right = n - 1

        inflation_point = self.binarySearch(left, right, nums)

        new_nums = nums[inflation_point : ] + nums[ : inflation_point]

        return new_nums == sorted_nums

    def binarySearch(self, left, right, nums):

        # Handle Duplicate Values
        while left < right and nums[left] == nums[right]:
            left += 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # The inflation point is on the right
                left = mid + 1
            elif nums[mid] <= nums[right]:
                # Mid can be the inflation point or the inflation point is on the left
                right = mid
        
        return left



# --------------------- Previous Element ---------------------------

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        count = 0

        for i in range(n):
            # previous index in circular sense
            prev_idx = (i-1) % n

            if nums[prev_idx] > nums[i]:
                count += 1
            
            # Ensure that there is only one inflation point
            if count > 1:
                return False
        
        return True