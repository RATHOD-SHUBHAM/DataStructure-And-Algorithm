class Solution:
    def __init__(self):
        self.op = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                self.threeSum(i, n, nums, target)
        
        return self.op
    
    def threeSum(self, i, n, nums, target):

        for j in range(i+1, n-2):
            if j == i + 1 or nums[j] != nums[j-1]:
                self.twoSum(i, j, n, nums, target)
    
    def twoSum(self, i, j, n, nums, target):
        left = j + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[j] + nums[left] + nums[right]

            if cur_sum > target:
                right -= 1
            
            elif cur_sum < target:
                left += 1
            
            else:
                self.op.append([nums[i] , nums[j] , nums[left] , nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            

        