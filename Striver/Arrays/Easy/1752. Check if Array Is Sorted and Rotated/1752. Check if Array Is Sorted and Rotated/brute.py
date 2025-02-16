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