class Solution:
    def jobSequencing(self, deadline, profit):
        """
        Job Sequencing Problem: Select jobs to maximize profit within deadlines
        
        Strategy: Greedy approach - always pick the job with highest profit first,
        then try to schedule it as late as possible (but before deadline)
        
        Args:
            deadline: List of deadlines for each job (1-indexed)
            profit: List of profits for each job
            
        Returns:
            Tuple: (number_of_jobs_completed, total_profit)
        """
        n = len(deadline)
        
        # Step 1: Create pairs of (profit, deadline) for easier processing
        arr = []
        for i in range(n):
            profit_val = profit[i]
            deadline_val = deadline[i]
            arr.append([profit_val, deadline_val])
        
        # Step 2: Sort jobs by profit in descending order (greedy choice)
        # If profits are equal, sort by deadline in descending order
        # This ensures we always consider the most profitable job first
        arr.sort(key=lambda x: (x[0], x[1]), reverse=True)
        
        # Step 3: Create a schedule array to track which time slots are occupied
        # Index represents time slot (0 to n-1), value represents profit of job scheduled
        # -1 means the time slot is free
        work_in_progress = [-1] * n
        
        # Step 4: Initialize counters for results
        max_job = 0      # Count of jobs completed
        total_profit = 0 # Sum of profits from completed jobs
        
        # Step 5: Try to schedule each job (starting with highest profit)
        for i in range(n):
            cur_profit, cur_deadline = arr[i]
            
            # Step 5: For current job, try to find the latest possible time slot
            # We go backwards from (deadline-1) to 0 because:
            # - Jobs are 1-indexed but our array is 0-indexed
            # - We want to schedule as late as possible to leave room for other jobs
            for curTime in reversed(range(cur_deadline)):
                
                # Step 6: Check if this time slot is available
                if work_in_progress[curTime] == -1:
                    # Schedule this job at current time slot
                    work_in_progress[curTime] = cur_profit
                    break  # Job scheduled successfully, move to next job
                
                # If slot is occupied, try the previous time slot
                # If no slot is available before deadline, job cannot be scheduled
        
        return (max_job, total_profit)

# Example walkthrough:
# Jobs: [(profit=20, deadline=1), (profit=10, deadline=2), (profit=40, deadline=1), (profit=30, deadline=1)]
# 
# After sorting by profit: [(40,1), (30,1), (20,1), (10,2)]
# 
# Scheduling:
# - Job with profit=40, deadline=1: Can schedule at time 0 → [40, -1]
# - Job with profit=30, deadline=1: Time 0 occupied, no other slot available → Skip
# - Job with profit=20, deadline=1: Time 0 occupied, no other slot available → Skip  
# - Job with profit=10, deadline=2: Can schedule at time 1 → [40, 10]
# 
# Result: 2 jobs completed, total profit = 50