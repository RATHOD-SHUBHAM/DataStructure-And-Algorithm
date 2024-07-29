class Solution:
    def countHomogenous(self, s: str) -> int:
        
        n = len(s)
        cnt = left = right = 0
        
        while left < n:
            while right < n and s[right] == s[left]:
                right += 1

            x = len(s[left : right])
            cnt += (x * (x+1)) // 2

            left = right
        
        MOD = (10**9) + 7
        return cnt % MOD