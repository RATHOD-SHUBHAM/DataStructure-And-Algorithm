# O(n^3) | Space: O(n)

def fourNumberSum(array, targetSum):
    def kSum(nums, target, k):
		res = []
		print("k : ",k)
		print("target : ",target)
		# If we have run out of numbers to add, return res.
		if not nums:
			return res
		print("nums: ",nums)
		# There are k remaining values to add to the sum. The 
		# average of these values is at least target // k.
		average_value = target // k

		print("average_value : ",average_value)

		# We cannot obtain a sum of target if the smallest value
		# in nums is greater than target // k or if the largest 
		# value in nums is smaller than target // k.
		if average_value < nums[0] or nums[-1] < average_value:
			print("res:s ",res)
			return res

		if k == 2:
			return twoSum(nums, target)

		for i in range(len(nums)):
			print("nums[i] : ",nums[i])
			# skip duplicate
			if i == 0 or nums[i - 1] != nums[i]:
				print("hi\n")
				for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
					print("subset is : ",subset)
					print("\n")
					res.append([nums[i]] + subset)
					print("PreFinal res: ",res)

		return res

	def twoSum(nums,target):
		res = []
		s = set()

		for i in range(len(nums)):
			if len(res) == 0 or res[-1][1] != nums[i]:
				if target - nums[i] in s:
					res.append([target - nums[i], nums[i]])
			s.add(nums[i])

		print("res for k = 2: ",res)
		return res

        
        
	array.sort()
	return kSum(array, targetSum, 4)
