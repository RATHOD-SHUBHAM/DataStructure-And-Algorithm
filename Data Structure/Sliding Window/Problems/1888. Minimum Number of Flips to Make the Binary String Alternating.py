# There will be 2 target 101010... or 010101010...

# compare the input with both the target and return the difference. -- return the one with minimum difference

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        s = s + s # make a copy of s so that it will check type one operation as well
        
        
        # The Two target
        targetOne = ""
        targetTwo = ""
        
        # differences
        diff = float("inf") # main difference to return
        diffOne = 0 # difference of individual target
        diffTwo = 0
        
        for i in range(len(s)):
            targetOne += "1" if i % 2 == 0 else "0"
            targetTwo += "0" if i % 2 == 0 else "1"
            
        # sliding Widow
        left = 0
        for right in range(len(s)):
            # Calculate the difference if there is a change on element
            if s[right] != targetOne[right]:
                diffOne += 1
            if s[right] != targetTwo[right]:
                diffTwo += 1
                
                
            # if the window size exceds move window
            if (right - left + 1) > n:
                # subtract one from diff only if we have added it out diff
                if s[left] != targetOne[left]:
                    diffOne -= 1
                if s[left] != targetTwo[left]:
                    diffTwo -= 1
                left += 1
                
            # calculate the actual diff when window is size n
            if (right - left + 1) == n:
                diff = min(diff,diffOne,diffTwo)
                
        return diff