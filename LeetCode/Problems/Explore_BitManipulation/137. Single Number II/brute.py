# Tc: O(n) | Sc: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        # print(counter)

        for val, count in counter.items():
            if count != 3:
                return val