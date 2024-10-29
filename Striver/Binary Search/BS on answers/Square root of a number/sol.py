class Solution:
    def floorSqrt(self, n): 
        left = 1
        right = n
        
        result = max_val = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            sqr_val = mid * mid
            
            
            if sqr_val <= n:
                if max_val < sqr_val:
                    max_val = sqr_val
                    result = mid
                
                left = mid + 1
            
            else:
                right = mid - 1
        
        return result