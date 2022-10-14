# https://www.youtube.com/watch?v=X0X6G-eWgQ8&ab_channel=takeUforward
# Tc and Sc: O(n)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        leftSmall = [0 for _ in range(n)]
        # print(leftSmall)
        rightSmall = [n for _ in range(n)]
        # print(rightSmall)
        
        # get the left smaller for each bar
        for i in range(n):
            
            # go on to left till you find element smaller than cur ele
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            # if the stack becomes empty
            if not stack:
                leftSmall[i] = 0
                stack.append(i)
                # print(stack)
            else:
                leftSmall[i] = stack[-1] + 1
                stack.append(i)
                
        # print(leftSmall)
        
        # clear the stack
        while stack:
            stack.pop()
        
        # find the right smaller element
        for i in reversed(range(n)):
            
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
                
            if not stack:
                rightSmall[i] = n - 1
                stack.append(i)
            else:
                rightSmall[i] = stack[-1] - 1
                stack.append(i)
                
        # print(rightSmall)
        
        # calculate maxArea
        maxArea = 0
        for i in range(n):
            curArea = heights[i] *( (rightSmall[i] - leftSmall[i]) + 1) # because we are dealing with index
            maxArea = max(maxArea ,curArea)
        
        return maxArea
            
        
            