'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


'''

# Time: O(n)
# Space: O(n)


# Sliding Window
# Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindowSize = 0
        
        dic = {} # to keep count of each occurance of character in given window
        
        left = 0 # window start point
        
        # window end point
        for right in range(len(s)):
            # Add the character count in dictionary
            if s[right] not in dic:
                dic[s[right]] = 1
            else:
                dic[s[right]] += 1
            
            # or
            # dic[s[right]] = 1 + dic.get(s[right],0)
            
            
            # Calculate window size
            windowSize = right - left + 1

            # Check the number of replacement available in the window
            # if there are no more replacement left
            if (windowSize) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            
            # recalculate windowSize
            windowSize = right - left + 1
            
            # Keep track of max window size
            maxWindowSize = max(maxWindowSize, windowSize)
            
        return maxWindowSize