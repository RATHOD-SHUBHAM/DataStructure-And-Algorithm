class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = i
        k = 1

        while j < n:
            if nums[i] == nums[j]:
                j += 1
            else:
                self.swap(k, j, nums)
                i = k
                k += 1
                j += 1
        
        # print(i)
        # print(nums)

        return i + 1
    
    def swap(self, k, j ,nums):
        nums[k] , nums[j] = nums[j], nums[k]
        return