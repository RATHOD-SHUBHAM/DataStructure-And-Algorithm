class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        jump_boundary = 0
        farthest = 0

        jump = 0

        for i in range(n-1):
            cur_jump = i + nums[i]
            farthest = max(farthest , cur_jump)

            if i == jump_boundary:
                jump += 1
                jump_boundary = farthest
        
        return jump