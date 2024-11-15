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