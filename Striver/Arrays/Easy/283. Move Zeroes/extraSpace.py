# Tc nad Sc: O(n)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ans = [0] * n

        j = 0
        for i in range(n):
            if nums[i] != 0:
                ans[j] = nums[i]
                j += 1
        
        nums[:] = ans[:]

        return nums