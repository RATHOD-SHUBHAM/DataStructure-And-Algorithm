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
    
# ------------------------------------------------------------------------------------------

# Tc: O(n) | Sc: O(1)

class Solution:
    def findTwoElement( self,arr, n): 
        Ts = (n * (n + 1)) // 2
        Ts_s = (n * (n + 1) * (2 * n + 1) ) // 6
        
        Cs = Cs_s = 0
        for i in range(n):
            Cs += arr[i]
            Cs_s += (arr[i] * arr[i])
        
        # x - y
        val_1 = Ts - Cs
        
        # (x-y)(x+y) 
        val_2 = Ts_s - Cs_s
        
        # x + y
        val_3 = val_2 // val_1

        # x
        x = (val_3 + val_1) // 2
        
        # y
        y = val_3 - x
        
        return [y, x]

