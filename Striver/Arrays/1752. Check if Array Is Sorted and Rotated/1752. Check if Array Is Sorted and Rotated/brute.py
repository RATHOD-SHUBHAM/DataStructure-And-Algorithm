'''
    rotate the array every time and check if it is sorted
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            if nums == sorted(nums):
                return True
            
            # rotate array once
            nums = nums[1 : ] + [nums[0]]

        return False