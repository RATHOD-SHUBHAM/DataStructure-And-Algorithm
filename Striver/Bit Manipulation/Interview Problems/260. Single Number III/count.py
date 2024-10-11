# Tc and Sc: O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)

        numbers = []
        for val, count in counter.items():
            if count == 1:
                numbers.append(val)
        
        return numbers


