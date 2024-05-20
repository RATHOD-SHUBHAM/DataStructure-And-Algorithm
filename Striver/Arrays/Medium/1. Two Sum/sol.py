class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            target = a + b
            b = target - a
        """
        n = len(nums)
        
        dict = {}
        
        for i in range(n):
            # b = target - a
            diff = target - nums[i]
            
            if diff in dict:
                return [dict[diff],i]
            
            dict[nums[i]] = i