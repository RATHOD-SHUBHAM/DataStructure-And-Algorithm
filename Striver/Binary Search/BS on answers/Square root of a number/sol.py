class Solution:
    def floorSqrt(self, n): 
        left = 1
        right = n 
        
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            sqrt = mid * mid
            
            if sqrt > n:
                right = mid - 1
            else:
                result = mid
                left = mid + 1
        
        return result