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
    
"""
The Core Idea:
    Instead of tracking individual jumps, we track "levels" or "waves" of reachability.
    Think of it like this: from your current position, you can reach a certain range of positions in one jump. 
    From any position in that range, you can reach another range in the next jump.

The key insight: 
    At each level, we need to consider ALL positions reachable with the current number of jumps to find the one that gives us the best reach for the NEXT jump. 
    We can't greedily pick the farthest position at each step because it might not lead to the optimal overall solution.

The algorithm essentially asks: 
    "Given that I can reach any position in range [a,b] with X jumps, what's the farthest I can reach with X+1 jumps?" 
    Only after exploring all positions in the current range does it commit to the next jump level.

Key Variables:
    jump_boundary: The farthest position reachable with the current number of jumps
    farthest: The farthest position we can reach if we make one more jump
    jump: The number of jumps taken so far

The Logic Flow:
    Explore all positions reachable with current jumps: 
        As we iterate through positions, we're exploring all positions reachable with our current jump count.
    
    Track the next level's potential: 
        For each position i, we calculate how far we could go if we jumped from there (i + nums[i]) and update farthest to track the maximum reach for the next jump level.
    
    Commit to the next jump when necessary: 
        When we reach jump_boundary (the limit of our current jump level), we must make another jump to continue. We increment jump and set the new boundary to farthest.

"""