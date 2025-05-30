class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        n = len(arr)

        abs_diff = math.inf
        for i in range(1, n):
            cur_diff = abs(arr[i-1] - arr[i])
            abs_diff = min(abs_diff , cur_diff)
        
        op = []
        for i in range(1, n):
            cur_diff = abs(arr[i-1] - arr[i])
            if cur_diff == abs_diff:
                op.append([arr[i-1] ,arr[i]])
        
        return op