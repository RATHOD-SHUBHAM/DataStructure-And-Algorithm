class Solution:
	def unsetBit(self, n):
		return n & (n - 1)