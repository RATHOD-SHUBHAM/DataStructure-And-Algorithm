class Solution:
    def findWaitingTime(self, jobs, n):
        jobs.sort()
        
        waiting_time = 0
        total_time = 0


        for i in range(n):
            waiting_time += total_time
            total_time += jobs[i]
        
        return (waiting_time , waiting_time // n)
    

if __name__ == "__main__":
    jobs = [2, 5, 1, 3, 4]
    n = len(jobs)
    
    solution = Solution()
    waiting_time, average_time = solution.findWaitingTime(jobs, n)
    
    print(f"Total waiting time: {waiting_time}")  # Output: Total waiting time: 10
    print(f"Average waiting time: {average_time}")  # Output: Average waiting time: 2



    jobs = [4,3,7,1,2]
    n = len(jobs)
    waiting_time, average_time = solution.findWaitingTime(jobs, n)
    print(f"Total waiting time: {waiting_time}")  # Output: Total waiting time: 10
    print(f"Average waiting time: {waiting_time // n}")  # Output: Average waiting time: 2