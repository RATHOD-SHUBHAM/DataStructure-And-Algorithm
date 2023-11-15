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
        