# Tc , Sc = O(n)

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        counter = {}
        
        for i in range(len(arr)):
            if arr[i] in counter:
                counter[arr[i]] += 1
            else:
                counter[arr[i]] = 1
        # print(counter)
        
        missing_number = duplicate_number = 0
        for i in range(1, n+1):
            if i not in counter:
                missing_number = i
            elif counter[i] > 1:
                duplicate_number = i
          
        
        return [duplicate_number , missing_number]