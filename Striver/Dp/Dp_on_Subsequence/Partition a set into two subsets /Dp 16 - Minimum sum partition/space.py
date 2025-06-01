#User function Template for python3
import math
class Solution:
    def minDifference(self, arr):
        # code here
        n = len(arr)
        
        total = sum(arr)
        
        dp = [False for _ in range(total+1)]
        
        # base case
        dp[0] = True
        dp[arr[0]] = True
        
        # Logic
        for idx in range(1, n):
            temp = [False for _ in range(total+1)]
            for cur_sum in range(1, total + 1):
                if cur_sum >= arr[idx]:
                    take = dp[cur_sum - arr[idx]]
                else:
                    take = False
                
                no_take = dp[cur_sum]
                
                temp[cur_sum] = take or no_take
            
            dp = temp
            dp[0] = True
        
        """
        The Last row of the DP table (the boolean array dp) represents all possible subset sums that can be achieved using elements from the input array.
        ie., if a particular sum can be obtained using all the elements in array
        """
        # print(dp[-1])
        
        min_diff = math.inf
        for cur_sum in range(total):
            if dp[cur_sum]:
                arr_1 = cur_sum
                arr_2 = total - cur_sum
                cur_diff = abs(arr_1 - arr_2)
                min_diff = min(min_diff, cur_diff)
                
        return min_diff

        