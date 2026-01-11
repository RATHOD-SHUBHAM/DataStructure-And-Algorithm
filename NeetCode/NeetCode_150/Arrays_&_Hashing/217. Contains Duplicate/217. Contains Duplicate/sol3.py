# Tc | Sc: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()

        for val in nums:
            if val in storage:
                return True
            else:
                storage.add(val)
        
        return False