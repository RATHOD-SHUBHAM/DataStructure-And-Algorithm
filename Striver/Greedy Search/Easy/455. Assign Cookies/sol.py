"""
Sort the childrens need and the cookie

eg: 
g = [3,1,4]
s = [2,3,1]

We need to be greedy, ie start by assigning smallest size cookie to the child and see if that satisfies the child
In order to do so, lets sort the array

g = [1, 3, 4] -> Sorting g help us, It checks if a particular cookie cannot satisfy here, then it will never satisfy anyone further
s = [1, 2, 3]

Now check one by one
s - satisfies -> g
* 1 satisfies 1
* 2 doesnot satisfy 3
* 3 satisfy 3

and we are out of cookie, so in total we can only satisy 2 children 1 and 3


# TC and SC
==============
Time Complexity: O(n⋅logn+m⋅logm) where n is the size of the array g and m is the size of the array s.
Sorting an array of length k takes O(k⋅logk), we need to sort two given arrays. The while loop iterates over each cookie and child once, taking O(m+n). To sum up, the overall time complexity is O(n⋅logn+m⋅logm)

Space Complexity: O(m+n) or O(logm+logn)
* Some extra space is used when we sort s and g in place. The space complexity of the sorting algorithm depends on the programming language.
* In Python, the sort method sorts a list using the Timesort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n+m) additional space.
* In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(logn+logm).

"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)

        g.sort()
        s.sort()

        chld_ptr = 0
        coki_ptr = 0

        while chld_ptr < m and coki_ptr < n:
            # if the cookie can satisfy the child, move to next
            if g[chld_ptr] <= s[coki_ptr]:
                chld_ptr += 1
                coki_ptr += 1
            else:
            # look for cookie that satisfy the current child
                coki_ptr += 1

        
        # Number of childeren who are satisfied
        if coki_ptr == n:
            return chld_ptr

        if chld_ptr == m:
            return m
        
# ----------------------- Same Solution -----------------------

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)

        g.sort()
        s.sort()

        chld_ptr = 0
        coki_ptr = 0

        while chld_ptr < m and coki_ptr < n:
            # if the cookie can satisfy the child, move to next
            if g[chld_ptr] <= s[coki_ptr]:
                chld_ptr += 1
            # look for cookie that satisfy the current child
            coki_ptr += 1

        
        # Number of childeren who are satisfied
        if coki_ptr == n:
            return chld_ptr

        if chld_ptr == m:
            return m
        

# ----------------------- Same Solution -----------------------


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)

        g.sort()
        s.sort()

        chld_ptr = 0
        coki_ptr = 0

        #or 
        while chld_ptr < m and coki_ptr < n:
            # if the cookie can satisfy the child, move to next
            if g[chld_ptr] <= s[coki_ptr]:
                chld_ptr += 1
            # look for cookie that satisfy the current child
            coki_ptr += 1

        
        # Number of childeren who are satisfied
        return chld_ptr
    
# ----------------------- Same Solution -----------------------
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        i = m - 1
        j = n - 1

        count = 0

        while i >= 0 and j >= 0:

            if s[j] >= g[i]:
                count += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        
        return count
    
# ----------------------- Same Solution -----------------------
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        i = m - 1
        j = n - 1

        count = 0

        while i >= 0 and j >= 0:

            if s[j] >= g[i]:
                count += 1
                j -= 1

            i -= 1
        
        return count