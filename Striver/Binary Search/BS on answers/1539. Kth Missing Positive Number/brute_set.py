class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)

        n = len(arr)

        cur_missing = k

        for i in range(n):
            if cur_missing < arr[i]:
                return cur_missing
            
            # if any number is present - push the missing number by one
            if arr[i] in set_arr:
                cur_missing += 1
        
        return cur_missing