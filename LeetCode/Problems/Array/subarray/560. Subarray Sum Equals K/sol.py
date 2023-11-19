# Tc and Sc :O(n)

# hashmap will tell us number of different ways we can form a substsring with value K till that particular index
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        
        # dic = (substring, count)
        dic = {0 : 1} # because if we have a singlke number eg 3 and k is 3 then 3 - 3 = 0. we then check how many substring are presnt. we cant write zero substring because 3 in itself is a substring , so we need to return 1. thats why we add count 1 for value 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            substring = prefix_sum - k
            
            if substring in dic:
                count += dic[substring]
            
            if prefix_sum not in dic:
                dic[prefix_sum] = 1
            else:
                dic[prefix_sum] += 1
                
        return count