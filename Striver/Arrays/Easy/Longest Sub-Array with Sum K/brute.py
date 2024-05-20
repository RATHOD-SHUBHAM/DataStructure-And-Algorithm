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
    

    