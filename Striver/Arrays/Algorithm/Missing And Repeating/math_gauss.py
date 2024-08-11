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