# Tc and Sc: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = collections.defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in dic:
                j = dic[nums[i]]
                diff = abs(i - j)

                if diff <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i
        
        return False
    
# -------------------------------- Clean Code --------------------------------
# Tc and Sc: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = collections.defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in dic:
                j = dic[nums[i]]
                diff = abs(i - j)

                if diff <= k:
                    return True
            
            dic[nums[i]] = i # Replace the number's index with the latest index
        
        return False