class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        # print(s)


# ------------------------- Two Pointers Approach -------------------------

# Tc:O(n) | Sc: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)

        i = 0
        j = n - 1

        while i < j:
            #swap i and j
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        