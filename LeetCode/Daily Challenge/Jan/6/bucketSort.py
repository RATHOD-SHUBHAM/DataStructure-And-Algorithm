class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maximun_no_of_icecream_bar = 0
        n = len(costs)
        
        max_costs = max(costs)
        countBucket = [0] * (max_costs + 1)
        m = len(countBucket)
        
        # add the number of count of each value in costs at its respective index in countBucket
        for i in range(n):
            cost = costs[i]
            countBucket[cost] += 1
        
        # print(countBucket)
        
        curCost = 0
        for cost in range(m):
            if cost == 0:
                continue
                
            # at some point my cost will exceed the available coins
            if cost > coins:
                break
            
            # either pick all the coins or limit it based on remaining coins
            all_coins = countBucket[cost]
            # if i have 4 coins and 2 of 3 cost - then. 4 // 3 = 1 - so out of 2 , 3 coins ill pick only 1
            pick_only = coins // cost 
            # this will be the frequency: ie no of ice cream picked
            cost_picked = min(all_coins , pick_only)
            
            
            curCost = cost * cost_picked
            
            coins -= curCost
            
            maximun_no_of_icecream_bar += cost_picked
            
        return maximun_no_of_icecream_bar
            
            
            
            
            