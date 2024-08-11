# ---------------------------- Brute Force ----------------------------

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1 and nums[0] == 0:
            return 1


        count = 0

        for i in range(n):
            xor = 0 ^ nums[i]

            for j in range(i+1, n):
                xor ^= nums[j]

                if xor == 0:
                    count += 1
        
        # print(count)
        return count
    

# ---------------------------- Dictionay ----------------------------

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
    

# ---------------------------- Using Get ----------------------------

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        dic = {0 : 1}

        xor = count = 0

        for i in range(n):
            xor ^= nums[i]
            count += dic.get(xor, 0)
            dic[xor] = dic.get(xor, 0) + 1
        
        return count