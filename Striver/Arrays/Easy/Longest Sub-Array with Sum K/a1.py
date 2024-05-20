# ------- Brute --------------------

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        cur_sum = 0
        
        max_len = 0
        
        left = right = 0
        
        while right < n:
            if cur_sum == k:
                str_len = (right - left)
                max_len = max(max_len , str_len)
                cur_sum -= arr[left]
                left += 1
            elif cur_sum > k:
                while left < right and cur_sum > k:
                    cur_sum -= arr[left]
                    left += 1
                cur_sum -= arr[right]
            else:
                cur_sum += arr[right]
                right += 1
        
        return max_len


# ---------- Math --------------------

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        dic = {}
        
        max_len = 0
        
        cur_sum = 0
        
        for right in range(n):
            
            cur_sum += arr[right] # y = x1 + x2
            
            if cur_sum == k:
                # first encounter of  sum == k
                max_len = right + 1
                
            elif cur_sum - k in dic:
                '''
                    y = x1 + x2
                    y - x2 = x1
                '''
                left = dic[cur_sum - k]
                
                cur_len = right - left
                
                max_len = max(max_len , cur_len)
            
            
            # add to dictionary
            if cur_sum not in dic:
                dic[cur_sum] = right
        
        return max_len