class Solution:
    def __init__(self):
        self.result = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
                
            if i == 0 or nums[i] != nums[i-1]:
                self.two_sum(i, n, nums)

        
        return self.result
    
    def two_sum(self, i: int, n:int, nums: List[int]) -> None:
        left = i + 1
        right = n - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]


            if cur_sum == 0:
                self.result.append([nums[i] , nums[left] , nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif cur_sum < 0:
                left += 1
            
            else:
                right -= 1
        
