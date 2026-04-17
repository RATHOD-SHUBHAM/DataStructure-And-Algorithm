# Tc and Sc: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        constraint = n / 3

        count = collections.Counter(nums)

        op = []

        for key, cnt in count.items():
            if cnt > constraint:
                op.append(key)
        
        return op
    
# ---------------------------------------: Boyer-Moore Logic :------------------------------------------------------------

"""
Observation:
At Max: we can have 2 element
At Min: there can be 0 maj ele

Eg: [4,4,4,3,3,3,1]
n = 8

so n / 3 = 2, we need to find element that are greater than 2

Now if we do 3 + 3 + 3: we will get 9, but n = 8
so 3 + 3 = 6 -> so at max we can have 2 elements
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count_1 = 0
        mode_1 = 0

        count_2 = 0
        mode_2 = 0

        for i in range(n):
            # Check if the number is not same as second number
            if count_1 == 0 and nums[i] != mode_2:
                mode_1 = nums[i]
            
            # Check if the number is not same as first number
            if count_2 == 0 and nums[i] != mode_1:
                mode_2 = nums[i]

            
            ## Voting
            # if the number is same increase count
            if nums[i] == mode_1:
                count_1 += 1
            
            elif nums[i] == mode_2:
                count_2 += 1
            
            # If number is not same decrease count
            else:
                count_1 -= 1
                count_2 -= 1
            
            # Saftey: if in case count goes less than 0: which will not happen but still reset it back
            if count_1 < 0:
                count_1 = 0
            if count_2 < 0:
                count_2 = 0
        


        ## Verification

        # Get the maj elements and its count
        maj_1 = maj_2 = 0
        for num in nums:
            if num == mode_1:
                maj_1 += 1
            elif num == mode_2:
                maj_2 += 1
        

        # Check if the maj element's count are greater than n / 3
        op = []
        if maj_1 > (n // 3):
            op.append(mode_1)
        if maj_2 > (n // 3):
            op.append(mode_2)
        

        return op