# tc and Sc = O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = 1
            
        return False