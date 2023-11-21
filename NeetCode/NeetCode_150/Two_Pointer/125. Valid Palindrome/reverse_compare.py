class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True 

        reversed_s = s[::-1]
        # print(reversed_s)

        lower_s = s.lower()
        # print(lower_s)
        lower_reversed_s = reversed_s.lower()
        # print(lower_reversed_s)

        n = len(lower_s)
        # print(n)
        
        i = 0
        j = 0

        while i < n and j < n:
            while i < n and not lower_s[i].isalnum():
                i += 1
            
            while j < n and not lower_reversed_s[j].isalnum():
                j += 1

            
            if i >= n or j >= n:
                break

            # print(lower_s[i] , lower_reversed_s[j])

            if lower_s[i] != lower_reversed_s[j]:
                return False
            
            i += 1
            j += 1
        
        return True