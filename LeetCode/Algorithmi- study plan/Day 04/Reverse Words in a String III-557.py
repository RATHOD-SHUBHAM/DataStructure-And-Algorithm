'''

557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.



'''

# Solution one
'''
Logic:
 Convert string to a list
 loop through list and  reverse each element
 join those reversed element into list

'''

p = []
print(s)

# convert string to list
s = s.split(" ")
print(s)

# loop through list and reverse each element
for i in s:
    print(i)
    i = i[::-1]
    print(i)
    p.append(i)
print(p)

# Join the reversed element
x = " ".join(p)
print(type(x))
print(x)




# solution 2: [one liner]
x =  " ".join([i[::-1] for i in s.split(" ")])
