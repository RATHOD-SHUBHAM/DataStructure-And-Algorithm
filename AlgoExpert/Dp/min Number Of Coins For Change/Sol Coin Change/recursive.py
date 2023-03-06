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