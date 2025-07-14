# Tc: O(2^n)
# Sc: O(n)

class Solution:
    def __init__(self):
        self.max_len = -math.inf
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)    

        def dfs(i, st):
            # base case
            if i == n:
                subseq = st[::]

                for i in range(1, len(subseq)):
                    if subseq[i-1] >= subseq[i]:
                        return

                cur_subseq_len = len(subseq)
                self.max_len = max(self.max_len, cur_subseq_len)
                return 
            
            # Logic
            st.append(nums[i])
            dfs(i+1, st)

            st.pop()
            dfs(i+1, st)

            return 
        
        i = 0
        st = []
        dfs(i, st)

        return self.max_len
    
# ------------------------------------ Recursion -------------------------------------
# Tc: O(2^n)
# Sc: O(n) for recursion stack space

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        prev_idx = -1

        return self.recursion(idx, prev_idx, n, nums)
    
    def recursion(self, idx, prev_idx, n, nums):
        # base case
        if idx == n:
            return 0
        
        # Logic
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            take = 1 + self.recursion(idx + 1, idx, n, nums)
        else:
            take = 0
        
        no_take = 0 + self.recursion(idx + 1, prev_idx, n, nums)

        return max(take, no_take)

# ------------------------------------ Memoization -------------------------------------
# Tc: O(n^2)
# Sc: O(n) for recursion stack space + O(n^2) for memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        idx = 0

        prev_idx = -1

        memo= {}

        return self.recursion(idx, prev_idx, memo, n, nums)
    
    def recursion(self, idx, prev_idx, memo, n, nums):
        # base case
        if idx == n:
            return 0
        
        if (idx, prev_idx) in memo:
            return memo[(idx, prev_idx)]
        
        # Logic
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            take = 1 + self.recursion(idx + 1, idx, memo, n, nums)
        else:
            take = 0
        
        no_take = 0 + self.recursion(idx + 1, prev_idx, memo, n, nums)

        memo[(idx, prev_idx)] = max(take, no_take)
        
        return memo[(idx, prev_idx)]
    
# ------------------------------------ Tabulation -------------------------------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

        for idx in reversed(range(n)):
            for prev_idx in reversed(range(-1, idx)):
                # Logic
                if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                    """
                    In the DP table, columns are labeled by prev_idx + 1.
                    So if your new prev_idx is idx, the column you jump to is (idx) + 1
                    """
                    take = 1 + dp[idx+1][idx+1] 
                else:
                    take = 0
                
                no_take = 0 + dp[idx+1][prev_idx+1]

                dp[idx][prev_idx+1] = max(take, no_take)

        return dp[0][0]
    
# ------------------------------------ Space Optimization -------------------------------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0 for _ in range(n+1)]

        for idx in reversed(range(n)):
            cur = [0 for _ in range(n+1)]
            for prev_idx in reversed(range(-1, idx)):
                # Logic
                if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                    take = 1 + dp[idx+1]
                else:
                    take = 0
                
                no_take = 0 + dp[prev_idx + 1]

                cur[prev_idx + 1] = max(take, no_take)
            
            dp = cur
                
        return dp[0]
    
# ------------------------------------ 1D DP -------------------------------------
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1 for _ in range(n+1)] # Every element is a subsequence of itself

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    take = 1 + dp[j] # add the cur number to previous LIS
                    dp[i] = max(dp[i], take)
        
        return max(dp)