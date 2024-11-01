# Push the scale
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num > k:
                return k
            else:
                k += 1
        return k