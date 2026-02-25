"""
Silly Mistakes To Take Care Of:

📌 There Is One Real Issue In Your Code

When we do .sort() on an array of strings, it sorts them in lexicographical order, not by length. 
So the first string after sorting is not necessarily the shortest string. 
This can lead to incorrect results when we assume that the first string is the common prefix.

Your comment says:

prefix = strs[0]  # max len of common prefix will be smallest char

This is NOT guaranteed to be the smallest string by length.

Sorting is lexicographic, not by length.

Example:

["aaab", "aa"]
↓ sort
["aa", "aaab"]

Here it works accidentally.

But sorting does NOT guarantee smallest length first.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() # nlogn
        
        prefix = strs[0] # the max len of common prefix will be len of our smallest char in worst case

        lcp = ""

        for i in range(len(prefix)):
            # Simulatenously iterate and compare each character
            for s in strs:
                if s[i] != prefix[i]:
                    return lcp
                
            lcp += prefix[i]


"""
Second Smallest Thing to Consider:

The question is asking for longest common prefix. The term prefix means the starting characters of the string.
This is something to pay attention to.

Let’s Test Your Concern
Input:
["dog","cog","pog"]

After sorting:

["cog","dog","pog"]

Now your logic:

prefix = "cog"

Compare index by index:

i = 0

Compare first character:

cog[0] = 'c'
dog[0] = 'd'   ← mismatch here

So we immediately return ""

Which is CORRECT.

Because there is no common prefix.

❗ Why You Thought It Would Fail

You were thinking:

They all have "og" at the end.

Yes — but that's a suffix, not a prefix.

The question asks for:

Longest common prefix

Prefix = starting characters.

So:

dog
cog
pog

All start with different letters → no common prefix.

So answer is "".

Your solution handles this correctly.

"""