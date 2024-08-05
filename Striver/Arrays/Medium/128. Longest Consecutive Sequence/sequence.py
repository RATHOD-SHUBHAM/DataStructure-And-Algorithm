class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        n = len(nums)

        LCS = 0

        sequence = []

        for i in range(n):
            cur_num = nums[i]

            if cur_num - 1 in num_set:
                continue
            
            count = 0
            cur_seq = []
            while cur_num in num_set:
                count += 1
                cur_seq.append(cur_num)
                cur_num += 1


            if count > LCS:
                LCS = count
                sequence[:] = cur_seq[:]

        print(sequence)
        return LCS