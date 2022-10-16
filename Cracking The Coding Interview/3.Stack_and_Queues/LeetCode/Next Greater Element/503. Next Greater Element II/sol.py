# https://www.youtube.com/watch?v=Du881K7Jtk8

# tc: O(n)
# Sc: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        nge = [-1] * n
        
        for i in reversed(range(2*n)):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                if stack:
                    nge[i] = stack[-1]
                else:
                    nge[i] = -1
            
            stack.append(nums[i % n])
            
        return nge