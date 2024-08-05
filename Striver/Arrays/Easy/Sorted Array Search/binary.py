# Tc: log(n) | Sc: O(1)

class Solution:
    ##Complete this function
    
    def searchInSorted(self,arr, N, K):
        #Your code here
        left = 0
        right = N - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == K:
                return 1
            elif arr[mid] < K:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1