"""
EPI Book:
Question 24.3 page 378

Buy and sell k times in a day

Also Follow uo to 122. Best Time to Buy and Sell Stock II
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that

        Knapsack/count: Number of allowed transaction
        A Transaction is complete only when i see a stock that i bought previously.
        """

        buy = True # This is my first stock, so i can think of purchasing this
        k = 2 # Count
        idx = 0

        memo = {}

        return self.recursion(idx, buy, k, memo, prices, n)
    
    def recursion(self, idx, buy, k, memo, prices, n):
        if idx == n:
            # if i would have bought a stock before and have not sold it
            # or there is no stock
            # Either way my profit will be 0
            return 0
        
        if k == 0:
            # I have no more transcation left for the terms
            # cant make any more profit
            return 0
        
        if (idx, buy, k) in memo:
            return memo[(idx, buy, k)]
        
        # Logic
        """
        Profit = sell - buy
        """
        if buy == True:
            # This mean i havent bought any stock in past
            # and I have the freedom to buy a stock or not buy any stock
            # K will remain unchanged as buying is not completing a transaction.

            # Change the bool value to buy stating we have a bought a stock
            purchase = self.recursion(idx+1, False, k, memo, prices, n) - prices[idx] # prices[idx]== buy, because this is the stock i buy

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = self.recursion(idx+1, True, k, memo, prices, n) - 0

            # Profit
            profit =  max(purchase , no_purchase)
        
        else:
            # This mean i have purhcased a stock previously and i can sell that
            # Selling mean a transaction is complete, so we can reduce k

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            sell = prices[idx] + self.recursion(idx+1, True, k - 1, memo, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            # Also, since we didnt sell transaction is not complete
            no_sell = 0 + self.recursion(idx+1, False, k, memo, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        memo[(idx, buy, k)] = profit

        return memo[(idx, buy, k)]