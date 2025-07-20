class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort() # makes the partition easy to process

        c = len(cuts)

        cuts = [0] + cuts[::]
        cuts.append(n)

        i = 1
        j = c

        memo = {}

        return self.recursion(i, j, memo, cuts)
    
    def recursion(self, i, j, memo, cuts):
        # Base case: no cuts between i and j
        if i > j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]
        
        min_cost = math.inf
        
        # Try making each cut between positions i and j
        for idx in range(i, j + 1):
            left_partition = self.recursion(i, idx - 1, memo, cuts)
            right_partition = self.recursion(idx + 1, j, memo, cuts)
            
            # Cost of current cut is the length of the segment
            cur_cost = cuts[j + 1] - cuts[i - 1]
            
            total_cost = left_partition + right_partition + cur_cost

            min_cost = min(min_cost , total_cost)
        
        
        memo[(i, j)] = min_cost
        return min_cost