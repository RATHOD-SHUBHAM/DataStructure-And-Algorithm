"""
EPI Book:
Question 24.3 page 378

Buy and sell k times in a day

Also Follow up to 122. Best Time to Buy and Sell Stock II
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        count = 2 # K transactions

        """
        Bool Buy: 0 or 1
        0: I have not purchased any stock previously, I am allowed to buy stock in future
        1: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        dp = [[0 for _ in range(count+1)] for _ in range(2)]

        # base case: if idx == n: return 0
        # for buy in range(2):
        #     for k in range(count+1):
        #         dp[n][buy][k] = 0
        
        # if count == 0: return 0
        for buy in range(2):
            dp[buy][0] = 0
            
        
        # Logic
        for idx in reversed(range(n)):
            temp = [[0 for _ in range(count+1)] for _ in range(2)]
            
            for buy in range(2):
                temp[buy][0] = 0

                for k in range(1, count+1):
                    if buy == 0:  # Can buy
                        # This mean i havent bought any stock in past
                        # and I have the freedom to buy a stock or not buy any stock
                        # K will remain unchanged as buying is not completing a transaction.

                        # Change the bool value to 1 stating we have bought a stock
                        purchase = dp[1][k] - prices[idx] # prices[idx]== buy, because this is the stock i buy

                        # The bool value is 0 stating I have not purchased any stock, I am allowed to buy stock in future
                        no_purchase = dp[0][k] - 0

                        # Profit
                        profit = max(purchase, no_purchase)
                    
                    else:  # buy == 1, must sell first
                        # This mean i have purchased a stock previously and i can sell that
                        # Selling mean a transaction is complete, so we can reduce k

                        # if i decide to sell, i can change the bool value to 0, stating I am allowed to buy stock in future
                        sell = prices[idx] + dp[0][k-1] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

                        # if i decide not to sell, I have a stock purchased previously,
                        # I cannot purchase any new one unless I sell the previous one
                        # Also, since we didnt sell transaction is not complete
                        no_sell = 0 + dp[1][k]

                        # Profit
                        profit = max(sell, no_sell)
                    
                    temp[buy][k] = profit
            
            dp = temp

        return dp[0][count]