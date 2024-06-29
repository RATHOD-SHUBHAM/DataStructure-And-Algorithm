#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        dic = {}
        
        max_len = 0
        
        cur_sum = 0
        
        for right in range(n):
            
            cur_sum += arr[right] # y = x1 + x2
            
            # first encounter of  sum == k
            if cur_sum == k:
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
                



