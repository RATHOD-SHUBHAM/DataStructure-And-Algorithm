# Freq Sort Logic

# Tc:O(n) | Sc: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = collections.Counter(nums)

        freq = [-math.inf] * (n+1)
        for key, cnt in count.items():
            freq[cnt] = key
        

        for ele in reversed(freq):
            if ele == -math.inf:
                continue
            else:
                return ele