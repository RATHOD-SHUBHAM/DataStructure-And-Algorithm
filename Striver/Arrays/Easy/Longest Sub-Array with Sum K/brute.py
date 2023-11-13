class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        max_len = 0
        
        for left in range(n):
            right = left
            
            cur_sum = 0
            while right < n:
            
                cur_sum += arr[right]
                
                if cur_sum == k:
                    cur_len = (right - left) + 1
                    max_len = max(max_len , cur_len)
                    break
                elif cur_sum > k:
                    break
                else:
                    right += 1
        
        return max_len