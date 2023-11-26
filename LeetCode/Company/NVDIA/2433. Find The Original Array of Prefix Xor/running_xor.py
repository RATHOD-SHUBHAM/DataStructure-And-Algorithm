# https://www.youtube.com/watch?v=idcT-p_DDrI&ab_channel=FisherCoder

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)

        arr = [pref[i] for i in range(n)]

        running_prefix = pref[0]

        for i in range(1, n):
            arr[i] = running_prefix ^ pref[i]
            running_prefix ^= arr[i]
            # print(running_prefix)
        
        # print(arr)
        return arr
