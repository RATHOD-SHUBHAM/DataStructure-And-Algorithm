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
