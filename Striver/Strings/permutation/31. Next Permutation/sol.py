class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        pivotIdx = -1

        for i in reversed(range(n-1)):
            if nums[i] < nums[i+1]:
                pivotIdx = i
                break
        
        if pivotIdx == -1:
            return nums.reverse()

        for i in reversed(range(pivotIdx, n)):
            if nums[i] > nums[pivotIdx]:
                nums[i] , nums[pivotIdx] = nums[pivotIdx] , nums[i]
                break
        
        nums[pivotIdx + 1 : ] = reversed(nums[pivotIdx + 1 : ])

        return nums