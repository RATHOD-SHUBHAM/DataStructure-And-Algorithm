# Tc: O(3n) = O(n) | Sc: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic = {}
        
        # get char count of s
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        
        # print(dic)
        
        # Check if t is present in s
        for char in t:
            if char in dic:
                dic[char] -= 1
            else:
                # if character is not present : they are not anagaram
                return False
        
        # print(dic)
        
        for char in dic:
            if dic[char] != 0:
                return False
        
        return True