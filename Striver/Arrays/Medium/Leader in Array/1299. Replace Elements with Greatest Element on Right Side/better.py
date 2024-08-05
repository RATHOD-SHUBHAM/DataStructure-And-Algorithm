class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        op = []
        op.append(-1)

        cur_greatest = arr[-1]

        for i in reversed(range(n-1)):
            op.append(cur_greatest)

            if arr[i] > cur_greatest:
                cur_greatest = arr[i]
        
        return op[::-1]