class Solution:
    def kthElement(self, k, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        
        cnt = p = q = 0
        
        while p < m and q < n:
            if arr1[p] < arr2[q]:
                cnt += 1
                if cnt == k:
                    return arr1[p]
                    
                p += 1
            else:
                cnt += 1
                if cnt == k:
                    return  arr2[q]
                    
                q += 1
        
        while p < m:
            cnt += 1
            if cnt == k:
                return arr1[p]
            
            p += 1
        
        while q < n:
            cnt += 1
            if cnt == k:
                return  arr2[q]
            
            q += 1