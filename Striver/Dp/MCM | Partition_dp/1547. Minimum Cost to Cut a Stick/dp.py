class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort() # makes the partition easy to process

        cuts = [0] + cuts[::]
        cuts.append(n)

        c = len(cuts) - 2 # Length of original cuts count before extension

        dp = [[0 for _ in range(c+2)] for _ in range(c+2)]

        # i = 1 # 1 -> c
        # j = c # c -> i
        for i in reversed(range(1, c+1)): # i: c, c-1, ..., 2, 1
            for j in range(i, c+1):
                if i > j:
                    continue

                min_cost = math.inf
        
                # Try making each cut between positions i and j
                for idx in range(i, j + 1):
                    left_partition = dp[i][idx-1]
                    right_partition = dp[idx+1][j]
                    
                    # Cost of current cut is the length of the segment
                    cur_cost = cuts[j + 1] - cuts[i - 1]
                    
                    total_cost = left_partition + right_partition + cur_cost

                    min_cost = min(min_cost , total_cost)
                
                
                dp[i][j] = min_cost
        
        # this will be the cut section
        return dp[1][c]