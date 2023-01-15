class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        
        total_cost = 0
        cur_cost = 0
        
        start_idx = 0
        for i in range(n):
            total_cost += gas[i] - cost[i]
            
            cur_cost += gas[i] - cost[i]
            
            if cur_cost < 0:
                cur_cost = 0
                start_idx = i + 1
                
        return start_idx if total_cost >= 0 else -1
        
                