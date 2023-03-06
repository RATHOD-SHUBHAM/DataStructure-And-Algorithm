# Logic: Use the current coin and dont use the current coin.
# backtracking
# # Tc and Sc: O(Exponential)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curAmount = 0
        curIdx = 0 # represent the coin at current Idx
        
        total_combination = [0]
        
        self.backTrack(curIdx, curAmount, coins, amount, total_combination)
        return total_combination[0]
    
    def backTrack(self, curIdx, curAmount, coins, amount, total_combination):
        # base case
        # if my curAmount match the target amont - then we found a combination
        if curAmount == amount:
            total_combination[0] += 1
            return
        # if my curAmount becomes greater than target amount
        if curAmount > amount:
            return 0
        
        # if my coin idx moves out of bound. ie i have explored all my coins
        if curIdx >= len(coins):
            return 0
        
        
        # logic code
        # use the current coin and check if we can reach the target
        newAmount = curAmount + coins[curIdx]
        self.backTrack(curIdx, newAmount, coins, amount, total_combination)
        
        # dont current coin and check if we can reach the target
        # in this case our curAmount will not change as we dont use the current coin
        self.backTrack(curIdx + 1, curAmount, coins, amount, total_combination)
        
        return 
        