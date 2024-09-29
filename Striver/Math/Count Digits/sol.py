class Solution:
    def evenlyDivides (self, N):
        count = 0
        last_digit = ""
        
        # Extract Last Digit
        while N > 0:
            last_digit += str(N % 10)
            N = N // 10
            count += 1
        
        return count