# DFS
# Time = O(coins * amount)
# Space = O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memoize
        dic = {} 
        
        minCoins = self.minCoins(coins,amount, dic)
        
        return minCoins if minCoins != float("inf") else -1
    
    
    def minCoins(self,coins, amount, dic):
        if amount not in dic:
            if amount == 0:
                return 0
            
            minCoin = float("inf")
            
            # check can you create a particular amount from these bunch of coin
            for coin in coins:
                cur_amount = amount - coin
                if cur_amount >= 0:
                    # 1 coin for the cur amount + no of coins for remaining amount
                    minCoin = min(minCoin, 1 + self.minCoins(coins, cur_amount, dic))
            
            
            # for a particular amount what was the minCoin needed out of all the bunch
            dic[amount] = minCoin
            # print("dic: ",dic)
            # print("\n")
            
        return dic[amount]