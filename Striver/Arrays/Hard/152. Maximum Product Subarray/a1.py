from typing import List

# ------------  Two run ----------

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_prod = -math.inf
        prefix_prod = suffix_prod = 1

        # Running prod
        ## Prefix : Left to Right
        for i in range(n):
            if prefix_prod == 0:
                '''
                    If there is a zero - reset the value
                '''
                prefix_prod = 1


            prefix_prod = prefix_prod * nums[i]
            max_prod = max(max_prod , prefix_prod)

        ## Suffix : Right to Left
        for i in reversed(range(n)):
            if suffix_prod == 0:
                '''
                    If there is a zero - reset the value
                '''
                suffix_prod = 1


            suffix_prod = suffix_prod * nums[i]
            max_prod = max(max_prod , suffix_prod)
        
        return max_prod
    

# ------------  Single run ----------

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_prod = -math.inf
        prefix_prod = suffix_prod = 1

        # Running prod
        for i in range(n):
            # If there is a zero - reset the value
            if prefix_prod == 0:
                prefix_prod = 1
            
            if suffix_prod == 0:
                suffix_prod = 1


            ## Prefix: Left to Right
            prefix_prod = prefix_prod * nums[i]

            ## Suffix : Right to Left
            x = n - i - 1
            suffix_prod = suffix_prod * nums[x]
            
            
            # Max of prefix or suffix prod
            maxi = max(prefix_prod , suffix_prod)
            max_prod = max(max_prod , maxi)
        
        return max_prod