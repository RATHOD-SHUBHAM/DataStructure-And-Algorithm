# tc and Sc: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic and (abs(dic[nums[i]] - i) <= k):
                return True
            dic[nums[i]] = i
        return False