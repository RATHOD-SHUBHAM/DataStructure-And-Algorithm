class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        n = len(nums)
        
        for i in range(n):
            m = len(subset)
            # print("len: ", m)
            for j in range(m):
                cur_set = subset[j] + [nums[i]]
                # print(cur_set)
                subset.append(cur_set)
        
        return subset