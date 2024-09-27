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