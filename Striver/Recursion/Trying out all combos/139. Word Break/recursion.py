# This will Time out

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        # Helper Function ---------
        def isValid(start):
            # base case
            if start == len(s):
                return True
            
            for end in range(start, len(s) + 1):
                cur_substring = s[start : end]
                # print(cur_break)

                if cur_substring in wordSet:
                    valid = isValid(end)

                    if valid == True:
                        return True
            
            return False


        # Main Function ---------
        valid = isValid(0)

        if valid == True:
            return True
        
        return False