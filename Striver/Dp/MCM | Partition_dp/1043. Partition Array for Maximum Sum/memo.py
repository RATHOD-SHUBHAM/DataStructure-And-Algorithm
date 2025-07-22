class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        i = 0

        memo = {}

        return self.recursion(i, k, n, memo, arr)
    
    def recursion(self, i, k, n, memo, arr):
        # base case
        if i == n:
            return 0
        
        if i in memo:
            return memo[i]
        
        # Logic
        max_sum = -math.inf

        max_ele = arr[i]

        end = min(n, i+k) # because if we are last index, i+k will go out of bound

        for j in range(i, end):

            max_ele = max(max_ele, arr[j])
            no_of_ele = j - i + 1

            cur_sum = no_of_ele * max_ele # [1, 15] = max = 15, len = 2 -> 15 * 2 = 15+15

            partition_sum = self.recursion(j+1, k, n, memo, arr)

            total_sum = cur_sum + partition_sum

            max_sum = max(max_sum, total_sum)
        
        memo[i] = max_sum
        return max_sum