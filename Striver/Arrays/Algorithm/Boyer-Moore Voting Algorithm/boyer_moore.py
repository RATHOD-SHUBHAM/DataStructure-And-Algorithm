# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        majority_ele = None

        for i in range(n):
            if count == 0:
                majority_ele = nums[i]
                count += 1
            
            elif nums[i] == majority_ele:
                count += 1
            else:
                count -= 1
        
        # You may assume that the majority element always exists in the array.
        return majority_ele

        '''
        # if there is no gurantee that majority element always exists then
        
        # check if this is the majority element
        count_of_majority_ele = 0
        for i in range(n):
            if majority_ele == nums[i]:
                count_of_majority_ele += 1
        
        if count_of_majority_ele > (n/2):
            return majority_ele
        else:
            return -1
        '''