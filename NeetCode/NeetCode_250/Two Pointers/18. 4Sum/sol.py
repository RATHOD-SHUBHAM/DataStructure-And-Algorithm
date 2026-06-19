class Solution:
    def __init__(self):
        self.op = []
    
    # Two Sum where input is sorted : 167. Two Sum II - Input Array Is Sorted
    def twosum(self, val, i, nums, target, n):

        j = i + 1
        k = n - 1

        while j < k:
            cur_sum = nums[i] + nums[j] + nums[k]


            if cur_sum == target:
                self.op.append([val, nums[i] , nums[j] , nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j-1]:
                    j += 1
                
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            
            elif cur_sum > target:
                k -= 1
            
            else:
                j += 1
        
        return


    # Three Sum: 15. 3Sum
    def threesum(self, val, idx, nums, target, n):

        for i in range(idx+1, n-2):
            if i == idx + 1 or nums[i] != nums[i-1]:
                self.twosum(val, i, nums, target, n)
        
        return 


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        # Break this down into small sub problem
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                diff = target - nums[i]
                self.threesum(nums[i], i, nums, diff, n)
        
        return self.op