class Solution:
    def count_no_of_substring(self, x):
        n = len(x)

        no_of_substring = (n * (n + 1)) // 2

        return no_of_substring
        

    def countHomogenous(self, s: str) -> int:
        
        n = len(s)
        cnt = left = right = 0
        
        while left < n:
            while right < n and s[right] == s[left]:
                right += 1
            
            cnt += self.count_no_of_substring(s[left : right])

            left = right
        
        MOD = (10**9) + 7
        return cnt % MOD

