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


