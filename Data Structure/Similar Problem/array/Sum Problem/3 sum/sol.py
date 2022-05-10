# time and space = O(n^2) | O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # since the number are sorted. The first number should be less than 0
            if nums[0] > 0:
                return res
            
            if i == 0 or nums[i] != nums[i-1]:
                self.two_sum(nums, res, nums[i], i)
                
        return res
                
    def two_sum(self, nums, res, first_num, idx):
        cache_set = set()

        j = idx + 1

        while j < len(nums):
            second_num = nums[j]
            third_num = 0 - second_num - first_num

            if third_num in cache_set:
                res.append([first_num, second_num, third_num])
                while j + 1 < len(nums) and nums[j+1] == nums[j]:
                    j += 1

            cache_set.add(second_num)
            j += 1
            
                