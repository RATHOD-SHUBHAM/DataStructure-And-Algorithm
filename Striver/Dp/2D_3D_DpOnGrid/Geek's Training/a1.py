# -------------------- Recursion --------------------
import math
class Solution:
    def maximumPoints(self, arr):
        # Code here
        no_of_tasks = len(arr[0]) # 3 = Running, Fighting, and Learning
        
        n = len(arr)
        
        prevs_day_task_idx = -1 # [No Task = -1, Running = 0, Fighting = 1, Learning = 2]
        
        return self.recursion(n-1, prevs_day_task_idx, no_of_tasks, arr)
    
    def recursion(self, idx, prevs_day_task_idx, no_of_tasks, arr):
        # base case
        if idx == 0:
            # get the max point based on the prevs_day_task
            max_points = -math.inf
            
            for cur_task in range(no_of_tasks):
                if cur_task == prevs_day_task_idx:
                    continue
                
                cur_points = arr[idx][cur_task]
            
                max_points = max(cur_points , max_points)
            
            return max_points
        
        # Consider all the task one after the other
        max_points = -math.inf
        for cur_task in range(no_of_tasks):
            if cur_task == prevs_day_task_idx:
                    continue
            
            cur_points = arr[idx][cur_task] + self.recursion(idx-1, cur_task, no_of_tasks, arr)
            
            max_points = max(cur_points , max_points)
        
        return max_points

# -------------------- Memoization --------------------

import math
class Solution:
    def maximumPoints(self, arr):
        # Code here
        no_of_tasks = len(arr[0]) # 3 = Running, Fighting, and Learning
        
        n = len(arr)
        
        prevs_day_task_idx = -1 # [No Task = -1, Running = 0, Fighting = 1, Learning = 2]
        
        memo = {} # [cur day, prev_days_task]
        
        return self.recursion(n-1, prevs_day_task_idx, memo, no_of_tasks, arr)
    
    def recursion(self, idx, prevs_day_task_idx, memo, no_of_tasks, arr):
        # base case
        if idx == 0:
            # get the max point based on the prevs_day_task
            max_points = -math.inf
            
            for cur_task in range(no_of_tasks):
                if cur_task == prevs_day_task_idx:
                    continue
                
                cur_points = arr[idx][cur_task]
            
                max_points = max(cur_points , max_points)
            
            return max_points
        
        if (idx, prevs_day_task_idx) in memo:
            return memo[(idx, prevs_day_task_idx)]
        
        # Consider all the task one after the other
        max_points = -math.inf
        for cur_task in range(no_of_tasks):
            if cur_task == prevs_day_task_idx:
                    continue
            
            cur_points = arr[idx][cur_task] + self.recursion(idx-1, cur_task, memo, no_of_tasks, arr)
            
            max_points = max(cur_points , max_points)
        
        
        # Memorize - current day and prev task
        memo[(idx, prevs_day_task_idx)] = max_points
        
        return memo[(idx, prevs_day_task_idx)]


# -------------------- Tabulation --------------------

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
    
# -------------------- Space Optimization --------------------

import math

class Solution:
    def maximumPoints(self, arr):
        # Code here
        no_of_tasks = len(arr[0]) # 3 = Running, Fighting, and Learning
        
        n = len(arr)
        
        if n == 1:
            return max(arr[0])
        
        dp = [0 for j in range(no_of_tasks)]
        
        # first row
        for i in range(no_of_tasks):
            dp[i] = arr[0][i]
        
        # Remaining days
        for i in range(1, n):
            temp = [0 for j in range(no_of_tasks)]
            # for every task
            for cur_task in range(no_of_tasks):
                # For each activity on day i, find best activity from day i-1
                for prev_day_task in range(no_of_tasks):
                    if prev_day_task == cur_task:
                        continue
                    
                    cur_point = arr[i][cur_task] + dp[prev_day_task]
                    
                    temp[cur_task] = max(temp[cur_task], cur_point)
            
            dp = temp
        
        """
        When you return dp[-1][-1], you're only returning the value at the last row, last column of your DP table.
        However, this might not be the optimal choice! The maximum points could be achieved by doing any of the three activities on the last day.
        """
        return max(dp)