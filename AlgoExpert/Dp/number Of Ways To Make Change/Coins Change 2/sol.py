# Time = O(ca) c is coins a is amount
# Space = O(a)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        
        dp[0] = 1
        
        for coin in coins:
            print("coin is: ",coin)
            for x in range(1,amount+1):
                print("amount is : ",x)
            # for coin in coins:
            #     print("coin : ",coin)
                if coin <= x:
                    dp[x] += dp[x - coin]
                    print(dp)
                    print("\n")
                    
        return dp[amount]