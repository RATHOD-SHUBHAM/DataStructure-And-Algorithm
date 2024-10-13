'''
Right Most Bit
One number above can set a bit
One number below can unset a bit
'''

# -------------------- Set Bit --------------------

class Solution:
	def setBit(self, n):
		return (n + 1) | n
	
# -------------------- Un-Set Bit --------------------
class Solution:
	def unsetBit(self, n):
		return n & (n - 1)