# Tc: O(n) | Sc: O(1)

# Dutch national land problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        left = 0 # keep track of 0's
        p = 0
        right = n - 1 # keep track of 2's

        while p <= right:
            if nums[p] == 0:
                self.swap(p, left, nums)
                left += 1
                p += 1
            elif nums[p] == 2:
                self.swap(p, right, nums)
                right -= 1
            else:
                p += 1
        
        return nums
    
    def swap(self, x, y, nums):
        nums[x], nums[y] = nums[y], nums[x]