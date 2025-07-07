class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        buy = True # This is my first stock, so i can think of purchasing this
        idx = 0

        """
        k : Cool Down Period
        True: We cannot purchase the stock
        False: We are allowed to purchase the stock
        """
        k = False

        memo = {}

        return self.recursion(idx, buy, k, memo, prices, n)
    
    def recursion(self, idx, buy, k, memo, prices, n):
        if idx == n:
            # if i would have bought a stock before and have not sold it
            # or there is no stock
            # Either way my profit will be 0
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

            # Check if we are not in any cool down period
            if k == False:
                # Change the bool value to buy stating we have a bought a stock
                purchase = self.recursion(idx+1, False, k, memo, prices, n) - prices[idx] # prices[idx]== buy, because this is the stock i buy
            else:
                purchase = -math.inf

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = self.recursion(idx+1, True, False, memo, prices, n) - 0

            # Profit
            profit =  max(purchase , no_purchase)
        
        else:
            # This mean i have purhcased a stock previously and i can sell that

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            # I also need to turn on cool down, so i cannot purchase a stock tomorrow
            sell = prices[idx] + self.recursion(idx+1, True, True, memo, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + self.recursion(idx+1, False, k, memo, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        memo[(idx, buy, k)] = profit

        return memo[(idx, buy, k)]


