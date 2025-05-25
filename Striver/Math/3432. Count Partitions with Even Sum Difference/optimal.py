# Tc: O(n)
# Sc: O(1)

""""
We know
arr_2 = total - arr_1 -> eq1
arr_1 - arr_2 = diff -> eq2


substituting eq1 in eq2
arr_1 - (total - arr_1) = diff
arr_1 - total - arr_1 = diff
2 * arr_1 - total = diff -> eq3

We know that any number multiplied by 2 is always even.

So we will only check if total is even, its doesnot matter if we are looking at -total or total, all that matter is if the number is even or not.
ie, -16 is also even and 16 is also even

therefore, form eq3 we check
total is even or not


we return n-1 , as we have to partition the array into 2
For an array of length n, the valid partition indices are:

i = 0: Left = [0], Right = [1, 2, ..., n-1]
i = 1: Left = [0, 1], Right = [2, 3, ..., n-1]
i = 2: Left = [0, 1, 2], Right = [3, 4, ..., n-1]
...
So there are exactly n-1 possible partition.

we return the total count of possible partitions, which is n-1
"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        if total % 2 == 0:
            return n - 1
        
        return 0