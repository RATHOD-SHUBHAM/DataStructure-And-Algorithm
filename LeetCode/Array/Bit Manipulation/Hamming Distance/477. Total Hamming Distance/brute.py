class Solution:
    def hammingDist(self, a , b):
        XOR = a ^ b
        return bin(XOR).count("1")
    
    def totalHammingDistance(self, nums: List[int]) -> int:
        cur_sum = 0
        
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                a = nums[i]
                b = nums[j]
                cur_sum += self.hammingDist(a,b)
        
        return cur_sum