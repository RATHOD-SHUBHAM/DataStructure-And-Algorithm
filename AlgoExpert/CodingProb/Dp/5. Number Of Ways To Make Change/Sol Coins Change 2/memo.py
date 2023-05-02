# Logic: Use the current coin and dont use the current coin.
# change the backtacking to recursive method to memoization - thus reducing time complexity
# Tc : O(amount * coins) | Sc: O(amount * coins) + O(amount)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curAmount = 0
        curIdx = 0 # represent the coin at current Idx
        
        # total_combination = [0]
        dp = [[None for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        
        return self.backTrack(curIdx, curAmount, coins, amount, dp)        
    # return total_combination[0]
    
    def backTrack(self, curIdx, curAmount, coins, amount, dp):
        # base case
        # if the value is already present
        if dp[curIdx][curAmount] != None:
            return dp[curIdx][curAmount]
            
        # if my curAmount match the target amont - then we found a combination
        if curAmount == amount:
            # total_combination[0] += 1
            return 1
        # if my curAmount becomes greater than target amount
        if curAmount > amount:
            return 0
        
        # if my coin idx moves out of bound. ie i have explored all my coins
        if curIdx >= len(coins):
            return 0
        
        
        # logic code
        # use the current coin and check if we can reach the target
        newAmount = curAmount + coins[curIdx]
        '''
        # backtracking
        self.backTrack(curIdx, newAmount, coins, amount, total_combination)
        
        # dont current coin and check if we can reach the target
        # in this case our curAmount will not change as we dont use the current coin
        self.backTrack(curIdx + 1, curAmount, coins, amount, total_combination)
        
        # recursive logic
        return self.backTrack(curIdx, newAmount, coins, amount) + self.backTrack(curIdx + 1, curAmount, coins, amount)
        '''
        
        if newAmount <= amount:
            # get the value with current coin and without including current coin
            dp[curIdx][curAmount] = self.backTrack(curIdx, newAmount, coins, amount, dp) + self.backTrack(curIdx + 1, curAmount, coins, amount, dp)
        
        else:
            # if the value is exceding the amount , dont include the current coin
            dp[curIdx][curAmount] = self.backTrack(curIdx + 1, curAmount, coins, amount, dp)
            
        return dp[curIdx][curAmount]