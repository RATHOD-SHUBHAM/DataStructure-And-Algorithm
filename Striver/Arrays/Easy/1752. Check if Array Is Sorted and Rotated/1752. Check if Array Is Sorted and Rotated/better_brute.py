class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 1

        inflation_point = 0

        while i < n:
            if nums[i-1] <= nums[i]:
                i += 1
            else:
                inflation_point = i
                break
        
        if nums[inflation_point :] + nums[ : inflation_point] == sorted(nums):
            return True
        else:
            return False