class Solution:
    def findXOR(self, l, r):
        xor = l

        for i in range(l + 1 , r + 1):
            xor = xor ^ i
        
        return xor
    

if __name__ == '__main__':
    obj = Solution()
    l = 4
    r = 8
    res = obj.findXOR(l , r)
    print(res)


# -------------- Algorithm XOR 1 - n --------------


'''
Use the idea: XOR of 2 number will be zero
eg: 2 ^ 2 = 0

So: xor from 3 to 5:
x1 = xor 1 to 3 = 1 ^ 2 
x2 = xor 1 to 5 = 1 ^ 2 ^ 3 ^ 4 ^ 5

x1 ^ x2 → will cancel out 1 ^ 2  and return 3 ^ 4 ^ 5

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
    