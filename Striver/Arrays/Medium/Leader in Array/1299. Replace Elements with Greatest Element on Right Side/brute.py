# Tc: TLE | Sc: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            if i == n - 1:
                arr[i] = -1
                continue

            max_value = max(arr[i+1 : ])
            arr[i] = max_value
        
        return arr