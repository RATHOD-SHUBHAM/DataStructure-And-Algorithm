class Solution:
    def GCD(self, a, b):
        if a == 0:
            return b
        return self.GCD(b%a, a)
    
    def LCM(self, a, b):
        return (a // self.GCD(a,b)) * b
        
    def lcmAndGcd(self, A , B):
        lcm = self.LCM(A,B)
        gcd = self.GCD(A, B)
    
        return [lcm,gcd]