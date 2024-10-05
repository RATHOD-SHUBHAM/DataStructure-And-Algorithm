class Solution:
    def countDigit (self, N):
        count = 0
        last_digit = ""
        
        # Extract Last Digit
        while N > 0:
            remainder = N % 10
            last_digit += str(remainder)
            N = N // 10
            count += 1
        
        return count