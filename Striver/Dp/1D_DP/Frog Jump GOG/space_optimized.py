import math
#User function Template for python3
class Solution:
    def minCost(self, height):
        n = len(height)
        
        # Base case
        if n < 2:
            return 0
        
        p_prev = 0 # Cost of jump at 0th step
        prev = abs(height[0] - height[1]) # cost of jump to 1st step
        
        for i in range(2, n):
            cost_jump_1 = prev + abs(height[i] - height[i-1])
            cost_jump_2 = p_prev + abs(height[i] - height[i-2])
            
            cur_cost = min(cost_jump_1, cost_jump_2)
            # Adjust index
            p_prev = prev
            prev = cur_cost
        
        return cur_cost
    
if __name__ == "__main__":
    height = [20, 30, 40, 20]
    obj = Solution()
    print(obj.minCost(height)) # Output: 20


    height = [10, 30, 40, 50, 20]
    obj = Solution()
    print(obj.minCost(height)) # Output: 50

    height = [10, 10, 10, 10]
    obj = Solution()
    print(obj.minCost(height)) # Output: 0
    
    height = [20, 30, 40, 30]
    obj = Solution()
    print(obj.minCost(height)) # Output: 10

    height = [319]
    obj = Solution()
    print(obj.minCost(height)) # Output: 0