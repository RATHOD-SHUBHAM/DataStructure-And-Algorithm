# Tc: O(n) | Sc: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        
        s_len = len(set_nums)
        
        n_len = len(nums)
        
        if n_len == s_len:
            return False
        else:
            return True