'''
    A number is odd if and only if its rightmost digit is odd.
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        left = 0
        right = n -1

        while right >= 0:
            if int(num[right]) % 2 != 0:
                return num[left : right + 1]
            
            right -= 1
        
        return ""