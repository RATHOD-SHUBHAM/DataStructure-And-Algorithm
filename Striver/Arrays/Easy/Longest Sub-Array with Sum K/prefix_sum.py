'''
Consider
    y = x1 + x2 where,
    
    y = total sum
    x1 = First element
    x2 = second element.

    we can write the above formula as,

    y - x2 = x1

    Here x2 = k

    so, if x1 is present in the dictionary, then x2 is the subset we are looking for.


Example:

    arr = [1,2,3]

    x1 = 1 + 2 = 3

    x2 = 3

    y = (1+2) + (3) = 6

    Now, if we are looking for k = 4

    then y - 4 = x1

    if x1 = 2 ? No, so we dont have a x2 as subset whose sum is 4

    Similarly, if k = 3

    y - 3 = x1,

    we have x1 = 3, so we know x2 wll be a subset of 3

So, here we will assume

x2 = k

y - k = x1, if x1 is there in dictionary, then x2 is a subset with value as k.

'''

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