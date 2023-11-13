class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        dic = {}
        
        cur_sum = 0
        max_len = 0
        
        for i in range(n):
            
            cur_sum += arr[i]
            
            if cur_sum == k:
                # first encounter of  sum == k
                max_len = i + 1
            
            elif cur_sum - k in dic:
                cur_diff = i - dic[cur_sum - k]
                max_len = max(max_len, cur_diff)
            
            
            if cur_sum not in dic:
                dic[cur_sum] = i
        
        return max_len