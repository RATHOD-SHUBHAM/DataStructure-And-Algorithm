# Tc: O(n) | Sc: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        
        farthestJump = 0
        goalPos = 0
        
        for curPos in range(n-1):
            #farthest distance
            farthestJump = max(farthestJump , curPos + nums[curPos])
            
            
            if curPos == goalPos:
                jumps += 1
                goalPos = farthestJump
        
        return jumps