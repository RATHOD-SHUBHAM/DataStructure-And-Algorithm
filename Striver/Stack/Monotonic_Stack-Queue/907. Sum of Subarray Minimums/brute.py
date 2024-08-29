# Tc: O(n^2) | Sc: O(1)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = (10 ** 9) + 7
        n = len(arr)

        sum_of_subarray = 0

        for i in range(n):
            cur_ele = arr[i]

            mini = cur_ele

            for j in range(i, n):
                mini = min(mini, arr[j])

                sum_of_subarray = (sum_of_subarray + mini) % MOD
        
        return sum_of_subarray