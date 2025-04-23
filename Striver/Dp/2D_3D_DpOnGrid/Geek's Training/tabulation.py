import math
class Solution:
    def maximumPoints(self, arr):
        # Code here
        no_of_tasks = len(arr[0]) # 3 = Running, Fighting, and Learning
        
        n = len(arr)
        
        if n == 1:
            return max(arr[0])
        
        dp = [[0 for j in range(no_of_tasks)] for i in range(n)]
        
        # first row
        for i in range(no_of_tasks):
            dp[0][i] = arr[0][i]
        
        # Remaining days
        for i in range(1, n):
            # for every task
            for cur_task in range(no_of_tasks):
                # For each activity on day i, find best activity from day i-1
                for prev_day_task in range(no_of_tasks):
                    if prev_day_task == cur_task:
                        continue
                    
                    cur_point = arr[i][cur_task] + dp[i-1][prev_day_task]
                    
                    dp[i][cur_task] = max(dp[i][cur_task], cur_point)
        
        """
        When you return dp[-1][-1], you're only returning the value at the last row, last column of your DP table.
        However, this might not be the optimal choice! The maximum points could be achieved by doing any of the three activities on the last day.
        """
        return max(dp[-1])