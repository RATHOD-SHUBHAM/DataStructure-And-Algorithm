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

# ----------------------------------------------------------------

# Tc: O(n^2) | Sc: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_set = set()

        n = len(nums)

        for i in range(n):
            a = nums[i]
            target = 0 - (a)

            dic = {}

            # 2 sum
            for j in range(i+1 , n):
                b = nums[j]
                diff = target - b

                if diff in dic:
                    # Handling Duplicate
                    temp = [a, b , diff]
                    temp.sort()
                    nums_set.add(tuple(temp))
                
                dic[b] = j
        
        # print(nums_set)
        for num in nums_set:
            ans.append(list(num))
        
        print(ans)


# ----------------------------------------------------------------

# Two Pointer: 2 Sum II

# Tc: O(n^2) | Sc: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)

        ans = []

        for i in range(n):
            a = nums[i]
            seen = set()

            if i == 0 or nums[i] != nums[i-1]:
                j = i+1

                while j < n:
                    # 2 sum 2 pointer
                    b = nums[j]
                    diff = -(a + b)

                    if diff in seen:
                        ans.append([a, b , diff])

                        # Skip the set to avoid duplicates
                        while j + 1 < n and nums[j] == nums[j+1]:
                            j += 1
                    
                    seen.add(b)
                    
                    j += 1
        return ans


