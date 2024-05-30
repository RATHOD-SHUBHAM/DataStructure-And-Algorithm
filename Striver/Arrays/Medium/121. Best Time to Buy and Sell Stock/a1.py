# Tc: O(n) | Sc: O(1)


#  ----------- Two Pass ----------------


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        buyDay = min(prices)
        idx_buyDay = prices.index(buyDay)

        print(buyDay, idx_buyDay)

        sellDay = -math.inf
        for i in range(idx_buyDay, n):
            cur_num = prices[i]

            if cur_num > sellDay:
                sellDay = cur_num
        
        return sellDay - buyDay
    
#  ----------- Single Pass ----------------

'''
    Profit is calculated as:
        Some_value - boughtPrice

    Max_profit is calculated as:
        max(max_profit, profit)

    So first we capture the boughtPrice - This value should be as less as possible
    then we calculate profit and check if this is a max_profit
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        boughtPrice = math.inf
        max_profit = 0

        for i in range(n):
            curPrice = prices[i]

            # Get the minimum Price
            if curPrice < boughtPrice:
                boughtPrice = curPrice
            
            # Calculate the profit
            profit = curPrice - boughtPrice

            # check the max_profit
            max_profit = max(profit, max_profit)
        
        return max_profit
        

#  ----------- OR ----------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        for i in range(1, n):
            # best time to buy is the smallest value prior this day
            best_buy = min(prices[ : i])

            profit = max(prices[i] - best_buy, profit)
        
        return profit