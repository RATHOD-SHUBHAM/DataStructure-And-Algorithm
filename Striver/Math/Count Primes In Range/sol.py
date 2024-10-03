class Solution:
    def seive(self, n):
        ref = [True] * (n+1)
        
        i = 2
        while i * i <= n:
            if ref[i] == True:
                x = i * i
                for j in range(x, n+1, i):
                    ref[j] = False
            
            i += 1
        
        return ref
    
    def countPrimes(self,L,R):
        #code here
        ref = self.seive(R)
        
        # print(ref)
        if L < 2:
            return ref[2:R+1].count(True)
        else:
            return ref[L:R+1].count(True)