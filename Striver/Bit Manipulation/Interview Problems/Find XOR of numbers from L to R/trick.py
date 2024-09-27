'''
1) Find XOR of the range [1, L – 1]. Let this be x1.
2) Find XOR of the range [1, R]. Let this be x2.
3) Return XOR of x1 and x2
'''

class Solution:
    def xor_1_n(self, n):
        mod = n % 4
        
        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        elif mod == 3:
            return 0
        
    def findXOR(self, l, r):
        x1 = self.xor_1_n(l - 1)
        x2 = self.xor_1_n(r)
        
        return x1 ^ x2
    