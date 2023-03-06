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