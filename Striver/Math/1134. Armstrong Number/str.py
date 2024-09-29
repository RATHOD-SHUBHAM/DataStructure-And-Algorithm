class Solution:
    def getPower(self, nums, k):
        power = 0

        for num in nums:
            x = int(num)
            power += (x ** k)
        
        return power
    
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        k = len(str_n)
        power_n = self.getPower(str_n, k)

        return n == power_n