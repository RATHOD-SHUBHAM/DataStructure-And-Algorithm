# O(n^3) | Space: O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        k = 4
        return self.k_sum(nums,target, k)
    
    def k_sum(self, nums, target, k):
        res = []
        
        # base case
        if not nums:
            return res
        
        # There are k remaining values to add to the sum. The 
        # average of these values is at least target // k.
        average_sum = target // k
        
        # We cannot obtain a sum of target if the smallest value
        # in nums is greater than target // k or if the largest 
        # value in nums is smaller than target // k.
        if average_sum < nums[0] or nums[-1] < average_sum:
            return res
        
        if k == 2:
            return self.two_sum(nums, target)
        
        # for greater than 2
        for i in range(len(nums)):
            # check for duplicates: if duplicates skip
            if i == 0 or nums[i] != nums[i-1]:
                # for every value that 2 sum return add it with current number
                for num in self.k_sum(nums[i+1 : ], target - nums[i], k-1):
                    res.append([nums[i]] + num)
                    
        return res
    
    def two_sum(self, nums, target):
        res = []
        cache_set = set()
        
        for i in range(len(nums)):
            # check for duplicates
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in cache_set:
                    res.append([target - nums[i] , nums[i]])
            
            cache_set.add(nums[i])
    
        return res
