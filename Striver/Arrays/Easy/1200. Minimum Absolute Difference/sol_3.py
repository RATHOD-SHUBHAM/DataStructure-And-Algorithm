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
