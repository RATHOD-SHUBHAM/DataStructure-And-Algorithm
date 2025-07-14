class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1 for _ in range(n+1)] # Every element is a subsequence of itself
        hash_idx = [i for i in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    take = 1 + dp[j] # add the cur number to previous LIS
                    
                    if take > dp[i]:
                        dp[i] = take
                        hash_idx[i] = j
                    
        
        LIS = []
        # print(dp.index(max(dp)))
        # print(hash_idx)
        idx = dp.index(max(dp))

        while hash_idx[idx] != idx:
            LIS.append(nums[idx])
            idx = hash_idx[idx]
        
        LIS.append(nums[idx])
        # print(LIS)

        return max(dp)



