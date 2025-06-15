class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        n = len(deadline)
        
        arr = []
        for i in range(n):
            arr.append([profit[i], deadline[i]])
        
        arr.sort(key = lambda x : (x[0], x[1]), reverse = True)
        
        visited = [-1] * n
        
        max_job = total_profit = 0
        for i in range(n):
            cur_profit, cur_deadline = arr[i]
            
            for j in reversed(range(cur_deadline)):
                if visited[j] == -1:
                    visited[j] = [cur_profit, i]
                    max_job += 1
                    total_profit += cur_profit
                    break
        
        return (max_job, total_profit)
        