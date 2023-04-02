# Tc and Sc: O(n)
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        max_idx = 0
        
        for i in range(n):
            no_of_idx = self.dfs(i, d, dp, arr)
            max_idx = max(max_idx, no_of_idx)
        
        return max_idx
        
    def dfs(self, i, d, dp, arr):
        # base case
        if i in dp: 
            return dp[i]

        max_path = 0

        # check the right jump
        for right in range(i + 1, i + d + 1):
            if right >= len(arr) or arr[right] >= arr[i]: 
                break
            right_path = self.dfs(right, d, dp, arr)

            max_path = max(max_path, right_path)

        # check the left jump
        # for left in reversed(range(i- d - 1, i)):
        for left in range(i - 1, i - d- 1, -1):
            if left < 0 or arr[left] >= arr[i]: 
                break
            left_path = self.dfs(left, d, dp, arr)

            max_path = max(max_path, left_path)

        dp[i] = max_path + 1 # +1 to include the current position
        return dp[i]