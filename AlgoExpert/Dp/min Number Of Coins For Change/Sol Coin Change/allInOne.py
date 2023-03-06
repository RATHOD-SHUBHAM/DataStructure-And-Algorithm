# ------------------------------------ Recursive ------------------------------------

# Tc and Sc: O(Exponential)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        curIdx = 0
        curAmount = 0
        minAmount = [math.inf]
        minCoinChange = self.recursion(curIdx, coins, curAmount, amount, minAmount)
        
        minAmount[0] = min(minAmount[0] , minCoinChange)
        if minAmount[0] == math.inf:
            return -1
        else:
            return minAmount[0]
        
    
    def recursion(self, curIdx, coins, curAmount, amount, minAmount):
        # base case
        if curIdx >= len(coins):
            return math.inf
        
        if curAmount > amount:
            return math.inf
        
        if curAmount == amount:
            return 0 # we have found a combination
        
        # Express recursion
        newAmount = curAmount + coins[curIdx]
        # Use the coin + dont use the coin
        
        if newAmount <= amount:
            takeCoin = 1 + self.recursion(curIdx, coins, newAmount, amount, minAmount)
            dontTakeCoin = 0 + self.recursion(curIdx + 1, coins, curAmount, amount, minAmount)
            
            minAmount[0] = min(takeCoin , dontTakeCoin)
        
        else:
            dontTakeCoin = 0 + self.recursion(curIdx + 1, coins, curAmount, amount, minAmount)
            
            minAmount[0] = dontTakeCoin
            
        return minAmount[0] 


# ------------------------------------ End of Recursive ------------------------------------

# ------------------------------------ Memoization ------------------------------------

# Tc: O(coins * amount) | Sc: O(coins * amount) * O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        curIdx = 0
        curAmount = 0
        memo = [[None for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        self.memoization(curIdx, coins, curAmount, amount, memo)
        # print("memo: ", memo)
        
        if memo[curIdx][curAmount] == math.inf:
            return -1
        else:
            return memo[curIdx][curAmount] if memo[curIdx][curAmount] is not None else 0 
    
    def memoization(self, curIdx, coins, curAmount, amount, memo):
        # base case
        if memo[curIdx][curAmount] != None:
            return memo[curIdx][curAmount]
        
        if curIdx >= len(coins):
            return math.inf
        
        if curAmount > amount:
            return math.inf
        
        if curAmount == amount:
            return 0 # we have found a combination
        
        # Express recursion
        newAmount = curAmount + coins[curIdx]
        # Use the coin + dont use the coin
        
        if newAmount <= amount:
            takeCoin = 1 + self.memoization(curIdx, coins, newAmount, amount, memo)
            dontTakeCoin = 0 + self.memoization(curIdx  + 1, coins, curAmount, amount, memo)
            
            memo[curIdx][curAmount] = min(takeCoin , dontTakeCoin)
        
        else:
            dontTakeCoin = 0 + self.memoization(curIdx  + 1, coins, curAmount, amount, memo)
            
            memo[curIdx][curAmount] = dontTakeCoin
            
        return memo[curIdx][curAmount]

# ------------------------------------ End of Memoization ------------------------------------



# ------------------------------------ 2D Dp ------------------------------------

# Tc: O(coins * amount) | Sc: O(coins * amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        # when i have 0 coin, i cannout make any amount
        # so the 0th row will be inf
        for col in range(amount + 1):
            dp[0][col] = math.inf
            
        # when i have some coins - I can make 0 amount by not using the coin
        for row in range(len(coins) + 1):
            dp[row][0] = 0
            
        # dp
        for coinIdx in range(1, len(coins) + 1):
            for curAmount in range(1, amount + 1):
                if curAmount >= coins[coinIdx - 1]:
                    # if i use the current amount - check for my remaining amount
                    remainingAmount = curAmount - coins[coinIdx - 1]
                    takeCoin = 1 + dp[coinIdx][remainingAmount]
                    dontTakeCoin = 0 + dp[coinIdx - 1][curAmount]
                    dp[coinIdx][curAmount] = min(takeCoin, dontTakeCoin)
                else:
                    dp[coinIdx][curAmount] =  dp[coinIdx - 1][curAmount]
                    
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1


# ------------------------------------ End of Dp ------------------------------------


# ------------------------------------ 1D Dp ------------------------------------

# Tc: O(coins * amount) | Sc: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        
            
        # dp
        for coinIdx in range(len(coins)):
            for curAmount in range(1, amount + 1):
                if curAmount >= coins[coinIdx]:
                    # if i use the current amount - check for my remaining amount
                    remainingAmount = curAmount - coins[coinIdx]
                    takeCoin = 1 + dp[remainingAmount]
                    dontTakeCoin = 0 + dp[curAmount]
                    dp[curAmount] = min(takeCoin, dontTakeCoin)
                else:
                    dp[curAmount] =  dp[curAmount]
                    
        return dp[-1] if dp[-1] != math.inf else -1


# ------------------------------------ End of Dp ------------------------------------
