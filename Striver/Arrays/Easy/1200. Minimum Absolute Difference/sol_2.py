class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        n = len(arr)

        abs_diff = math.inf
        op = []
        
        for i in range(1, n):
            cur_diff = abs(arr[i-1] - arr[i])

            if cur_diff == abs_diff:
                op.append([arr[i-1] ,arr[i]])
            elif cur_diff < abs_diff:
                abs_diff = cur_diff
                op = [[arr[i-1] ,arr[i]]]
        
        return op