class Solution:
    def count_number(self, n):
        count = 0
        while n > 0:
            count += 1
            n = n // 10
        return count
    
    def getPower(self, nums, k):
        power = 0

        for num in nums:
            x = int(num)
            power += (x ** k)
        
        return power
    
    def isArmstrong(self, n: int) -> bool:
        k = self.count_number(n)
        power_n = self.getPower(str(n), k)

        return n == power_n