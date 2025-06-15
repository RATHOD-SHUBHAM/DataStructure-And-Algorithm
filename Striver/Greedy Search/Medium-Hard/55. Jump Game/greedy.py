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
            
            if max_pos >= n-1:
                return True
        
        return False