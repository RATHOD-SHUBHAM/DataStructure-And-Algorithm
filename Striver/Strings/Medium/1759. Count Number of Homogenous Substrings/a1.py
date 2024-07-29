# -----------  Find the Substring ------------------

class Solution:
    def no_of_substring(self, x):
        n = len(x)
        substring = []

        for i in range(n):
            for j in range(i, n):
                substring.append(x[j:])
        
        return len(substring)

    def countHomogenous(self, s: str) -> int:
        
        n = len(s)
        cnt = left = right = 0
        
        while left < n:
            while right < n and s[right] == s[left]:
                right += 1
            
            cnt += self.no_of_substring(s[left : right])

            left = right
        
        return cnt




# -----------  Just Counting the Substring ------------------

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





# -----------  Single Function ------------------

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