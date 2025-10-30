# ----------------- Using sorting -----------------
# Tc: O(N log N) | Sc: O(1)
class Solution:
    def largest(self, arr):
        # code here
        arr.sort()
        return arr[-1]
    
# ----------------- Using built-in function -----------------
# Tc: O(N) | Sc: O(1)
def largest( arr, n):
    return max(arr)

# ----------------- Using linear traversal -----------------
# Tc: O(N) | Sc: O(1)
class Solution:
    def largest(self, arr):
        # code here
        n = len(arr)
        
        largest_ele = arr[0]
        
        for i in range(1, n):
            if arr[i] > largest_ele:
                largest_ele = arr[i]
        
        return largest_ele