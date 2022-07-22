'''

792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.


'''
# Bucket creation method


#Tc: O(s.length + words[i].length)
# Sc: O(words.length)


# creating a dict with list
from collections import defaultdict, deque
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # creating bucket
        bucket = defaultdict(lambda: deque( [] ) )
        # adding value into bucket based on the first character
        for word in words:
            bucket[word[0]].append(word)
            
        no_of_subseq = 0
        # go through each word in s and check if word is a subsequence of s
        for char in s:
            # for the particular char
            for i in range(len(bucket[char])):
                word = bucket[char].popleft()
                
                # there is a complete match
                if len(word) == 1:
                    no_of_subseq += 1
                    continue
                
                # append the remaing ele in the bucket
                bucket[word[1]].append(word[1: ])
                
        return no_of_subseq