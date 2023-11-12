class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] , nums[i] = nums[i] , nums[j]
                j += 1 # keep track of where zero is - and next time swap that pos with non zero val

        return nums
        