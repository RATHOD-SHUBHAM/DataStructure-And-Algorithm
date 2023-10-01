# Tc: O(n^3) | Sc: O(1)

# This will add duplicate values as well to our answer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if(nums[i] + nums[j] + nums[k]) == 0:
                        ans.append([nums[i] , nums[j] , nums[k]])
        
        print(ans)


# ----------------------------------------------------------------

# taking care of duplicate values
'''
    Sort + Set -> will help save unique values
'''

# Tc: O(n^3) | Sc: O(nlogn)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_set = set()
        
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if(nums[i] + nums[j] + nums[k]) == 0:
                        # Taking care of duplication
                        temp = [nums[i] , nums[j] , nums[k]]
                        temp.sort()
                        nums_set.add(tuple(temp))

        for num in nums_set:
            ans.append(list(num))
        
        print(ans)

