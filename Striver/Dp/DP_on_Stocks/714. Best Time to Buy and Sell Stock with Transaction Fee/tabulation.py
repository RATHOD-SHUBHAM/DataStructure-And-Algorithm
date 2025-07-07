class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        dp = [[0 for _ in range(2)]for _ in range(n+1)]

        # base case, idx == n: return 0
        for j in range(2):
            dp[n][j] = 0
        
        # Logic
        for idx in reversed(range(n)):
            for buy in range(2): # assume 0 is True and 1 is False
                # Logic
                """
                Profit = sell - buy
                """
                if buy == 0:
                    # This mean i havent bought any stock in past
                    # and I have the freedom to buy a stock or not buy any stock

                    # Change the bool value to buy stating we have a bought a stock
                    purchase = dp[idx+1][1] - prices[idx] # prices[idx]== buy, because this is the stock i buy

                    # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
                    no_purchase = dp[idx+1][0] - 0

                    # Profit
                    profit =  max(purchase , no_purchase)
                
                else:
                    # This mean i have purhcased a stock previously and i can sell that

                    # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
                    sell = prices[idx] + dp[idx+1][0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)
                    sell -= fee

                    # if i decide not to sell, I have a stock purchased previously,
                    # I cannot purchase any new one unless I sell the previous one
                    no_sell = 0 + dp[idx+1][1]

                    # Profit
                    profit = max(sell , no_sell)
                
                dp[idx][buy] = profit

        return dp[0][0]