# ------------------------------  Two Loop  ------------------------------

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
    

# ------------------------------  One Loop  ------------------------------

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

# ------------------------------  One Loop with Dictionary  ------------------------------

# Tc: O(nlogn) | Sc: O(n)

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        dic = collections.defaultdict(list)

        arr.sort()

        for i in range(1, n):
            cur_diff = abs(arr[i-1] - arr[i])

            dic[cur_diff].append([arr[i-1], arr[i]])
        
        # print(dic)
        # print(min(dic.keys()))

        min_key = min(dic.keys())

        return dic[min_key]
