# https://www.youtube.com/watch?v=X0X6G-eWgQ8&ab_channel=takeUforward
# tc = O(n^3)
# sc: O(1)


# brute force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        # for each block start finding max area
        for i in range(len(heights)):
            # get the width
            for j in range(i , len(heights)):
                minHeight = inf
                # get the min height up until now
                for k in range(i , j+1):
                    minHeight = min(minHeight , heights[k])
                    
                maxArea = max(maxArea , minHeight * (j - i + 1))
                
        return maxArea
        