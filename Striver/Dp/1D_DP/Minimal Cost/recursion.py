import math

#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        # Since the arr is 0 based index, the last element will be at position n-1
        return self.recursion(n-1, k, arr)
        
    def recursion(self, n, k, arr):
        # base case
        if n == 0:
            return 0
        
        min_cost = math.inf
        for i in range(1, k+1):
            if n - i < 0:
                break
            
            
            cur_cost = self.recursion(n-i, k, arr) + abs(arr[n] - arr[n-i])
        
            
            min_cost = min(min_cost, cur_cost)
        
        return min_cost
    
if __name__ == "__main__":
    # Example usage
    k = 3
    arr = [10, 30, 40, 50, 20]
    obj = Solution()
    print(obj.minimizeCost(k, arr))  # Output: 30