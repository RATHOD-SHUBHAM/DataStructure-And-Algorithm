# Tc: O(n) | Sc: O(1)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        greatest = arr[n-1]

        for i in reversed(range(n)):
            if arr[i] >= greatest:
                cur_num = arr[i]
                arr[i] = greatest
                greatest = cur_num
                continue
            
            arr[i] = greatest
        
        arr[n-1] = -1

        return arr