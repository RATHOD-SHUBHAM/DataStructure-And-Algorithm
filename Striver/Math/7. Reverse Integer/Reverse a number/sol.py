class Solution:
    def reverse_number (self, N):
        count = 0
        new_number = 0
        
        # Extract Last Digit
        while N > 0:
            remainder = N % 10
            new_number = new_number * 10 + remainder
            N = N // 10
            count += 1
        
        print(new_number)
        return count