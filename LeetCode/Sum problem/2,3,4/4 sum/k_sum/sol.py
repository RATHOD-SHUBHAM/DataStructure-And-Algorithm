class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        k = 4
        return self.k_sum(nums, target , k)
    
    def k_sum(self, nums, target, k):
        quadruplets = []
        
        if not nums:
            return quadruplets
        
        # health check
        avg_target = target // k
        
        if avg_target < nums[0] or nums[-1] < avg_target:
            return quadruplets
        
        # check for two sum
        if k == 2:
            return self.two_sum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                for pairs in self.k_sum(nums[i+1 : ], target - nums[i], k -1):
                    quadruplets.append( [nums[i]] + pairs )
                    
        return quadruplets
    
    def two_sum(self, nums, target):
        dic = {}
        pair = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in dic and (len(pair) == 0 or pair[-1][1] != nums[i]):
                pair.append([diff , nums[i]])
                
            dic[nums[i]] = i
            
        return pair