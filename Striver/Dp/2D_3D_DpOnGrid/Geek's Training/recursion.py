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