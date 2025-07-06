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
        if idx == n:
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
            sell = prices[idx] + self.recursion(idx+1, True, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + self.recursion(idx+1, False, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        return profit

# -------------------------------- Memoization Code -------------------------

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
        if idx == n:
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
            sell = prices[idx] + self.recursion(idx+1, True, memo, prices, n) # prices[idx]== sell, so equation will be like sell - buy + (future profit)

            # if i decide not to sell, I have a stock purchased previously,
            # I cannot purchase any new one unless I sell the previous one
            no_sell = 0 + self.recursion(idx+1, False, memo, prices, n)

            # Profit
            profit = max(sell , no_sell)
        
        memo[(idx, buy)] = profit

        return memo[(idx, buy)]
    

# --------------------------------  Tabulation Code -------------------------

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

                    # if i decide not to sell, I have a stock purchased previously,
                    # I cannot purchase any new one unless I sell the previous one
                    no_sell = 0 + dp[idx+1][1]

                    # Profit
                    profit = max(sell , no_sell)
                
                dp[idx][buy] = profit

        return dp[0][0]

# --------------------------------  Space Optimized Code -------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        """
        Bool Buy: True or False
        True: I have not purchased any stock previously, I am allowed to buy stock in future
        False: I cannot purchase a stock, because i have a stock i previously purchased and have to first sell that
        """

        dp = [0 for _ in range(2)]

        # base case, idx == n: return 0
        # dp = 0
        
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
                    purchase = dp[1] - prices[idx] # prices[idx]== buy, because this is the stock i buy

                    # The bool value is True stating I have not purchased any stock, I am allowed to buy stock in future
                    no_purchase = dp[0] - 0

                    # Profit
                    profit =  max(purchase , no_purchase)
                
                else:
                    # This mean i have purhcased a stock previously and i can sell that

                    # if i decide to sell, i can change the bool value to true, stating I am allowed to buy stock in future
                    sell = prices[idx] + dp[0] # prices[idx]== sell, so equation will be like sell - buy + (future profit)

                    # if i decide not to sell, I have a stock purchased previously,
                    # I cannot purchase any new one unless I sell the previous one
                    no_sell = 0 + dp[1]

                    # Profit
                    profit = max(sell , no_sell)
                
                dp[buy] = profit

        return dp[0]
    
    
# ------------------------- Greedy Code -------------------------

# Tc: O(n)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        i = 0 
        total_profit = 0

        while i < n:
            # For every valley
            buy = prices[i]

            max_profit = 0
            j = i + 1

            # Capture the peak
            while j < n:
                # Check for peak
                if prices[j] > prices[j-1]:
                    profit = prices[j] - buy
                    
                    max_profit = max(max_profit, profit)

                    j += 1
                else:
                    # If there is a dip
                    break
            
            # Gather the profit
            total_profit += max_profit
            i = j

        return total_profit


# ------------------------- Optimized Code -------------------------

"""
Instead of looking for every peak following a valley, 
we can simply go on crawling over the slope and keep on adding the profit obtained from every consecutive transaction. 
In the end,we will be using the peaks and valleys effectively, 
but we need not track the costs corresponding to the peaks and valleys along with the maximum profit, 
but we can directly keep on adding the difference between the consecutive numbers of the array if the second number is larger than the first one, and at the total sum we obtain will be the maximum profit.
"""

# Tc: O(n)
# Sc: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        total_profit = 0

        for i in range(1, n):
            # If price goes up, capture the profit
            if prices[i] > prices[i-1]:
                profit = prices[i] - prices[i-1]
                total_profit += profit
        
        return total_profit