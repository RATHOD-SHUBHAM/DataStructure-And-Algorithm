'''
Eg: "Hello World!"
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        count = 0
        start = 0
        maxLen = 0
        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            count = i - start + 1
            maxLen = max(maxLen,count)
            
            dic[s[i]] = i
            
        return maxLen