class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        pos = 0
        score = nums[0]
        
        max_score = self.dfs(pos, score, k, nums)
        
        return max_score
    
    def dfs(self, pos, score, k, arr):
        # base case
        if pos == len(arr) - 1:
            return score
        
        max_score = 0
        for nxt_pos in range(pos + 1, pos + k + 1):
            if nxt_pos < len(arr):
                new_score = score + arr[nxt_pos]
                new_score = self.dfs(nxt_pos, new_score, k, arr)
                
                max_score = max(max_score, new_score)
    
        return max_score