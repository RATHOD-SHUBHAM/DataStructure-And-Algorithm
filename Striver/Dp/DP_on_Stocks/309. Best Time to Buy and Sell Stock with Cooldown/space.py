class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        k : Cool Down Period
        True = 0: We cannot purchase the stock
        False = 1: We are allowed to purchase the stock
        """
        cooldown = 2 # True or false

        dp = [[0 for _ in range(cooldown)] for _ in range(2)]


        # Logic
        for idx in reversed(range(n)):
            temp = [[0 for _ in range(cooldown)] for _ in range(2)]
            for buy in range(2):
                for k in range(cooldown):
                    """
                    Profit = sell - buy
                    """
                    if buy == 0:
                        # This mean i havent bought any stock in past
                        # and I have the freedom to buy a stock or not buy any stock

                        # Check if we are not in any cool down period
                        if k == 1:
                            # Change the bool value to buy stating we have a bought a stock
                            purchase = dp[1][k] - prices[idx] # prices[idx]== buy, because this is the stock i buy
                        else:
                            purchase = -math.inf

                        # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
                        no_purchase = dp[0][1] - 0

                        # Profit
                        profit =  max(purchase , no_purchase)
                    
                    else:
                        # This mean i have purhcased a stock previously and i can sell that

                        # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
                        # I also need to turn on cool down, so i cannot purchase a stock tomorrow
                        sell = prices[idx] + dp[0][0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

                        # if i decide not to sell, I have a stock purchased previously,
                        # I cannot purchase any new one unless I sell the previous one
                        no_sell = 0 + dp[1][k]

                        # Profit
                        profit = max(sell , no_sell)
                    
                    temp[buy][k] = profit
            
            dp = temp

        return dp[0][1]
    