# Time = O(nlogn) + O(klogk)
# Space = O(n)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # time = O(nlogn)
        # Space = O(n)
        sorted_arr = sorted(arr, key = lambda a : abs(x - a))
        print(sorted_arr)
        
        # O(klogk)
        sorted_arr = sorted_arr[ : k]
        
        return sorted(sorted_arr)