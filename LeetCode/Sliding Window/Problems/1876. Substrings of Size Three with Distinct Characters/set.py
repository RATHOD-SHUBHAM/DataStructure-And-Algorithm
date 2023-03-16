class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n-2):
            # print(set(s[i : i+3]))
            # print(len(set(s[i:i+3])))
            
            if len(set(s[i:i+3])) == 3:
                count += 1
                
        # print(count)
        return count