# https:https://www.youtube.com/watch?v=jC_cWLy7jSI&ab_channel=takeUforward
# Tc and Sc: O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        n = len(heights)
        
        for i in range(n):
            
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curHeight = heights[stack.pop()]
                curWidth = i - stack[-1] - 1
                curArea = curHeight * curWidth
                
                maxArea = max(maxArea , curArea)
            
            stack.append(i)
            
        # once we finish iteration we will still have some element in stack
        while stack[-1] != -1:
            curHeight = heights[stack.pop()]
            curWidth = n - stack[-1] - 1
            curArea = curHeight * curWidth
                
            maxArea = max(maxArea , curArea)
        
        return maxArea