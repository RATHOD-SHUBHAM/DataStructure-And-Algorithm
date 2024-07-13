# Tc: O(n) | Sc: O(1)

# Dutch national land problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        p0 = 0
        left = 0
        right = n - 1

        while left <= right:

            if nums[left] == 2:
                nums[left] , nums[right]  = nums[right] , nums[left]
                right -= 1
            elif nums[left] == 0:
                nums[p0], nums[left] = nums[left] , nums[p0]
                left += 1
                p0 += 1
            else:
                left += 1
        
        return nums