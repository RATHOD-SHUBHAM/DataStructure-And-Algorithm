class Solution:
    def maxLen(self, n, arr):
        k = 0
        dic = {0 : -1} # Store the index
        
        cur_sum = max_len = 0
        
        for i in range(n):
            cur_sum += arr[i]
            
            diff = cur_sum - k
            
            if diff in dic:
                left = dic[diff]
                right = i
                
                cur_len = right - left
                max_len = max(max_len , cur_len)
            
            if cur_sum not in dic:
                dic[cur_sum] = i
        
        return max_len