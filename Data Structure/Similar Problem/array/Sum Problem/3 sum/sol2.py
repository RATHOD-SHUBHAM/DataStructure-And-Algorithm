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
        left = idx + 1
        right = len(nums) - 1
        
        while left < right:
            cur_sum = first_num + nums[left] + nums[right]
            
            if cur_sum > 0:
                right -= 1
            elif cur_sum < 0:
                left += 1
            else:
                res.append([first_num, nums[left], nums[right]])
                
                # adjust pointer
                left += 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1