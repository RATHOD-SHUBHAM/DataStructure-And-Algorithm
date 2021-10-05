"""
49. Group Anagrams

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


"""

strs = ["eat","tea","tan","ate","nat","bat"]
_dict = {}

"""
for words in strs:
    sortedwords = sorted(words)
    print(sortedwords)
    
    If i just do sorted each value will be seperated as a lsit . In order to convert them into a str we use join
    op:
    
    ['a', 'e', 't']
    ['a', 'e', 't']
    ['a', 'n', 't']
    ['a', 'e', 't']
    ['a', 'n', 't']
    ['a', 'b', 't']
"""


for words in strs:
    sortedwords = "".join(sorted(words))
    # print(sortedwords)
    if sortedwords in _dict:
        # append in dictionary of list
        _dict[sortedwords].append(words)
    else:
        _dict[sortedwords] = [words]
    # print(_dict)

result = []
for val in _dict.values():
    # print(val)
    result.append(val)
    print(result)