class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0

        return self.recursion(idx, n, nums)
    
    def recursion(self, idx, n, nums):
        # base case
        if idx == n-1:
            return True
        
        if idx >= n:
            return False
        
        if nums[idx] == 0:
            # we cannot move further
            return False
        
        # Logic
        canJump = False
        for jump in range(1, nums[idx] + 1):
            curJump = self.recursion(idx + jump, n, nums)
            canJump = canJump or curJump
        
        return canJump

# ------------------------------ Memoization ------------------------------

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        idx = 0

        memo = {}

        return self.recursion(idx, memo, n, nums)
    
    def recursion(self, idx, memo, n, nums):
        # base case
        if idx == n-1:
            return True
        
        if idx >= n:
            return False
        
        if nums[idx] == 0:
            # we cannot move further
            return False

        if idx in memo:
            return memo[idx]
        
        # Logic
        canJump = False
        for jump in range(1, nums[idx] + 1):
            curJump = self.recursion(idx + jump, memo, n, nums)
            canJump = canJump or curJump
        
        memo[idx] = canJump

        return memo[idx]

# ------------------------------ Tabulation ------------------------------
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [False for _ in range(n)]

        # base case
        dp[n-1] = True

        for i in reversed(range(n-1)):
            # Base
            if nums[i] == 0:
                dp[i] = False
                continue
            
            # Logic
            canJump = False
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    curJump = dp[i + jump]
                    canJump = canJump or curJump
            
            dp[i] = canJump
        
        return dp[0]
    
# ------------------------------ Greedy ------------------------------

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        # Base case
        if n == 1:
            return True
        
        if nums[0] == 0:
            return False

        # For each position, check what is the maximum distance we can reach
        # If we can reach the last postion, then we can return true

        max_pos = 0

        for i in range(n-1):
            # Check is current position is reachable from the start
            if i > max_pos:
                return False

            cur_jump_dist = i + nums[i]

            if cur_jump_dist > max_pos:
                max_pos = cur_jump_dist
            
            # We will reach last position even if max jump > n-1, can it hops across the last position
            if max_pos >= n-1:
                return True
        
        return False