class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        dic = {0: 1}

        xor = 0
        count = 0

        for i in range(n):
            xor ^= nums[i]
            
            if xor in dic:
                count += dic[xor]
                dic[xor] += 1
            else:
                dic[xor] = 1
        
        return count
    
# ----------------   Using DefaultDict   -----------------------------

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        dic = collections.defaultdict(int)
        dic[0] = 1

        xor = 0
        count = 0

        for i in range(n):
            xor ^= nums[i]
            
            if xor in dic:
                count += dic[xor]
            
            dic[xor] += 1
        
        return count