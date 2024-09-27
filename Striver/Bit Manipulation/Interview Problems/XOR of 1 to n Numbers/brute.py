class Solution:
    def findXOR(self, n):
        xor = 0

        for i in range(1, n + 1):
            xor = xor ^ i
        
        return xor
    

if __name__ == '__main__':
    obj = Solution()
    n = 8
    res = obj.findXOR(n)
    print(res)