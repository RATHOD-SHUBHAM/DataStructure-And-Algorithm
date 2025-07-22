class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        i = 0

        return self.recursion(i, k, n, arr)
    
    def recursion(self, i, k, n, arr):
        # base case
        if i == n:
            return 0
        
        # Logic
        max_sum = -math.inf

        max_ele = arr[i]

        end = min(n, i+k) # because if we are last index, i+k will go out of bound

        for j in range(i, end):
            
            max_ele = max(max_ele, arr[j])
            no_of_ele = j - i + 1

            cur_sum = no_of_ele * max_ele # [1, 15] = max = 15, len = 2 -> 15 * 2 = 15+15

            partition_sum = self.recursion(j+1, k, n, arr)

            total_sum = cur_sum + partition_sum

            max_sum = max(max_sum, total_sum)
        
        return max_sum