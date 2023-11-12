'''
2- pointer:
    Lock the position where we want to insert : we want to insert right after the unique number
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        insertPosition = 1
        idx = 1

        while idx < n:
            # if not dulicate
            if nums[idx] != nums[idx - 1]:
                # this is the next position after unique character
                nums[insertPosition] = nums[idx]
                insertPosition += 1

            idx += 1
        
        # print(insertPosition)
        return insertPosition
        

            
            



        