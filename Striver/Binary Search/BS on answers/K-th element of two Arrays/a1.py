class Solution:
    def kthElement(self, k, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        
        sorted_array = []
        
        p = q = 0
        
        while p < m and q < n:
            if arr1[p] < arr2[q]:
                sorted_array.append(arr1[p])
                p += 1
            else:
                sorted_array.append(arr2[q])
                q += 1
        
        sorted_array += arr1[p : ] + arr2[q : ]

        return sorted_array[k-1]
    

# ----------------------- Better -----------------------

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


# ----------------------- Optimized -----------------------


import math
class Solution:
    def kthElement(self, k, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        
        left_side = k
        
        left = max(0, k - n)
        right = min(k, m)
        
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = left_side - mid1
            
            l1 = l2 = -math.inf
            r1 = r2 = math.inf
            
            if mid1 < m:
                r1 = arr1[mid1]
            if mid2 < n:
                r2 = arr2[mid2]
            if mid1 - 1 >= 0:
                l1 = arr1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = arr2[mid2 - 1]
            
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1