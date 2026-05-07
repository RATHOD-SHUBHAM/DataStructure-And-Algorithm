# Tc and Sc: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        dic = {}

        for i in range(n):

            # If the current element is alredy in dictionary : Duplicate 
            # Check the difference of their index
            if nums[i] in dic and abs(i - dic[nums[i]]) <= k:
                return True
            
            dic[nums[i]] = i # Store along with the index
        
        return False