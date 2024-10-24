class Solution:
    def __init__(self):
        self.op = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, nums, n)
            
        
        return self.op
    
    def twoSum(self, i, nums, n):
        left = i + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == 0:
                self.op.append([nums[i] , nums[left] , nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                
            elif cur_sum > 0:
                right -= 1
            
            else:
                left += 1