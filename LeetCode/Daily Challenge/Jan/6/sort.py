#Tc: O(n log n) | Sc: O(n)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort() # O(n) space for sorting
        n = len(costs)
        
        maximun_no_of_ice_cream_bar = 0
        cost_of_ice_cream_bar = 0
        for i in range(n):
            if cost_of_ice_cream_bar + costs[i] > coins:
                break
            
            cost_of_ice_cream_bar += costs[i]
            maximun_no_of_ice_cream_bar += 1
        
        return maximun_no_of_ice_cream_bar