class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        # print(dic)

        for _, val in dic.items():
            if val > 2:
                return False
        return True