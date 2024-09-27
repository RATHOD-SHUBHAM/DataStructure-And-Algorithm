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

# --------------------------------------------

'''
When we do XOR of numbers, we get 0 as the XOR value just before a multiple of 4. This keeps repeating before every multiple of 4. 

1- Find the remainder of n by moduling it with 4. 
2- If rem = 0, then XOR will be same as n. 
3- If rem = 1, then XOR will be 1. 
4- If rem = 2, then XOR will be n+1. 
5- If rem = 3 ,then XOR will be 0.

'''

class Solution:
    def findXOR(self, n):
        mod = n % 4

        if mod == 0:
            return n
        elif mod == 1:
            return 1
        elif mod == 2:
            return n + 1
        elif mod == 3:
            return 0
    

if __name__ == '__main__':
    obj = Solution()
    n = 8
    res = obj.findXOR(n)
    print(res)