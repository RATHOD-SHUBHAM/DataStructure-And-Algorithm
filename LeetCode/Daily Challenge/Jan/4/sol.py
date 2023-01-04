# Tc and Sc: O(n)

from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksCounter = Counter(tasks)
        n = len(tasks)
        
        # for i in range(n):
        #     tasksCounter[tasks[i]] += 1
        # this part cant be written as Counter(tasks)
        
        
        minRounds = 0
        
        for task, val in tasksCounter.items():
            # base case
            if val == 0:
                continue
                
            # cant complete of the task count if it is less than 2
            if val < 2:
                return -1
            else:
                # keep removing task till the value becomes 0
                while val > 0:
                    # it makes sense to remove max value inorder to get minimum steps
                    if val - 3 == 0 or val - 3 >= 2:
                        tasksCounter[task] = val - 3
                        minRounds += 1
                        val = tasksCounter[task]
                    else:
                        tasksCounter[task] = val - 2
                        minRounds += 1
                        val = tasksCounter[task]
        
        return minRounds