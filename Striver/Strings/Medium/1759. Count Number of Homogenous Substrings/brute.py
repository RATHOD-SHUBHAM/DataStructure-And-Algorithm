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

