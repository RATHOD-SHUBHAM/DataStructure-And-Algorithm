# Tc: O(1) | Sc: O(n)

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        arr_set = set(arr)
        
        if K in arr_set:
            return 1
        else:
            return -1
