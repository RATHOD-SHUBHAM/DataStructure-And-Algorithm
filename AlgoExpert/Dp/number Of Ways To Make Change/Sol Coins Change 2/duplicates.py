# This solution causes duplication - Which should not be the case
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total_sum = [0]
        curAmount = 0
        
        total_sum[0] += self.recursive(curAmount, coins, amount, total_sum)
        
        return total_sum[0]
    
    def recursive(self, curAmount, coins, amount, total_sum):
        # base case
        if curAmount == amount:
            return 1
        if curAmount > amount:
            return 0
        
        for coin in coins:
            print("coin: ", coin)
            newAmount = curAmount + coin
            print("newAmount: ", newAmount)
            total_sum[0] += self.recursive(newAmount, coins, amount, total_sum)
            print(total_sum)
        
        print("\n")
        return total_sum[0]