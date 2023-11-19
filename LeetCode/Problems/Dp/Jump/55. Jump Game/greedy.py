# Tc:O(n) | Sc:O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalPos = n - 1
        
        for curIdx in reversed(range(n-1)):
            farthestJump = curIdx + nums[curIdx]
            
            # check if i can jump to my goal position
            if farthestJump >= goalPos:
                # then check if i can reach the current position from other remaining index
                goalPos = curIdx
                
        # if my goal pos becomes index 0 . then from there I can reach the end
        return goalPos == 0