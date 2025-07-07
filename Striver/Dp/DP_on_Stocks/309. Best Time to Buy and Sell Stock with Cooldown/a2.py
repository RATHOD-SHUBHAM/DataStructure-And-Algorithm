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

        return self.recursion(idx, buy, prices, n)
    
    def recursion(self, idx, buy, prices, n):
        if idx >= n:
            # if i would have bought a stock before and have not sold it
            # or there is no stock
            # Either way my profit will be 0
            return 0
        
        # Logic
        """
        Profit = sell - buy
        """
        if buy == True:
            # This mean i havent bought any stock in past
            # and I have the freedom to buy a stock or not buy any stock

            # Change the bool value to buy stating we have a bought a stock
            purchase = self.recursion(idx+1, False, prices, n) - prices[idx] # prices[idx]== buy, because this is the stock i buy

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = self.recursion(idx+1, True, prices, n) - 0

            # Profit
            profit =  max(purchase , no_purchase)
        
        else:
            # This mean i have purhcased a stock previously and i can sell that

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            # after selling I can apply cool down by skipping the next day and jumping to dayafter.
            sell = prices[idx] + self.recursion(idx+2, True, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + self.recursion(idx+1, False, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        return profit
    

# ------------------------- Memoization Approach -------------------------

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

        memo = {}

        return self.recursion(idx, buy, memo, prices, n)
    
    def recursion(self, idx, buy, memo, prices, n):
        if idx >= n:
            # if i would have bought a stock before and have not sold it
            # or there is no stock
            # Either way my profit will be 0
            return 0
        
        if (idx, buy) in memo:
            return memo[(idx, buy)]
        
        # Logic
        """
        Profit = sell - buy
        """
        if buy == True:
            # This mean i havent bought any stock in past
            # and I have the freedom to buy a stock or not buy any stock

            # Change the bool value to buy stating we have a bought a stock
            purchase = self.recursion(idx+1, False, memo, prices, n) - prices[idx] # prices[idx]== buy, because this is the stock i buy

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = self.recursion(idx+1, True, memo, prices, n) - 0

            # Profit
            profit =  max(purchase , no_purchase)
        
        else:
            # This mean i have purhcased a stock previously and i can sell that

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            # after selling I can apply cool down by skipping the next day and jumping to dayafter.
            sell = prices[idx] + self.recursion(idx+2, True, memo, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + self.recursion(idx+1, False, memo, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        memo[(idx, buy)] = profit

        return memo[(idx, buy)]


# ------------------------- Tabulation Approach -------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        dp = [[0 for _ in range(2)]for _ in range(n+2)]

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
                    # after selling I can apply cool down by skipping the next day and jumping to dayafter.
                    sell = prices[idx] + dp[idx+2][0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

                    # if i decide not to sell, I have a stock purchased previously,
                    # I cannot purchase any new one unless I sell the previous one
                    no_sell = 0 + dp[idx+1][1]

                    # Profit
                    profit = max(sell , no_sell)
                
                dp[idx][buy] = profit

        return dp[0][0]
    
# -------------------------  Same solution removing for loop -------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        dp = [[0 for _ in range(2)]for _ in range(n+2)]

        # base case, idx == n: return 0
        for j in range(2):
            dp[n][j] = 0
        
        # Logic
        for idx in reversed(range(n)):
            # The buy loop runs for 0 and 1 -> instead of looping we can hardcode the value
            # for buy in range(2): # assume 0 is True and 1 is False
            # Logic
            """
            Profit = sell - buy
            """
            # if buy == 0:
            # This mean i havent bought any stock in past
            # and I have the freedom to buy a stock or not buy any stock

            # Change the bool value to buy stating we have a bought a stock
            purchase = dp[idx+1][1] - prices[idx] # prices[idx]== buy, because this is the stock i buy

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = dp[idx+1][0] - 0

            # Profit
            profit =  max(purchase , no_purchase)
            dp[idx][0] = profit
            
            # else:
            # This mean i have purhcased a stock previously and i can sell that

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            # after selling I can apply cool down by skipping the next day and jumping to dayafter.
            sell = prices[idx] + dp[idx+2][0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + dp[idx+1][1]

            # Profit
            profit = max(sell , no_sell)
            
            dp[idx][1] = profit

        return dp[0][0]

# ------------------------- Space Optimized Approach -------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        # 3 Pointers
        cur = [0] * 2 # idx
        front_1 = [0] * 2 # idx + 1
        front_2 = [0] * 2 # idx + 2
        
        # Logic
        for idx in reversed(range(n)):
            # The buy loop runs for 0 and 1 -> instead of looping we can hardcode the value
            # for buy in range(2): # assume 0 is True and 1 is False
            # Logic
            """
            Profit = sell - buy
            """
            # if buy == 0:
            # This mean i havent bought any stock in past
            # and I have the freedom to buy a stock or not buy any stock

            # Change the bool value to buy stating we have a bought a stock
            purchase = front_1[1] - prices[idx] # prices[idx]== buy, because this is the stock i buy

            # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
            no_purchase = front_1[0] - 0

            # Profit
            profit =  max(purchase , no_purchase)
            cur[0] = profit
            
            # else:
            # This mean i have purhcased a stock previously and i can sell that

            # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
            # after selling I can apply cool down by skipping the next day and jumping to dayafter.
            sell = prices[idx] + front_2[0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + front_1[1]

            # Profit
            profit = max(sell , no_sell)
            cur[1] = profit

            # Swap pointers for next iteration
            front_2 = front_1 # neighbor becomes next neighbor
            front_1 = cur # current becomes neighbor
            cur = [0] * 2


        return front_1[0]