class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    

'''

❌ Common Wrong Answers:
	nums = sorted(set(nums))
	return len(nums)

    nums =  doesn't replace elements in the original list.
nums[:] = replaces element in place


'''