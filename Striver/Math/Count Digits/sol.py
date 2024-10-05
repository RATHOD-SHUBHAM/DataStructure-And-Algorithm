class Solution:
    def evenlyDivides (self, N):
        # code here
        copy_n = N
        count = 0
        
        while N > 0:
            remainder = N % 10
            
            if remainder > 0 and copy_n % remainder == 0:
                count += 1
            
            N = N // 10
        
        return count