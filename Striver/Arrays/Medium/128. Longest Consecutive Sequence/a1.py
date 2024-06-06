# --------------- Without sequence ---------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        num_set = set(nums)

        max_count = 0

        for i in range(n):
            cur_num = nums[i]

            if cur_num - 1 not in num_set:
                count = 1

                while cur_num + 1 in num_set:
                    count += 1

                    cur_num = cur_num + 1
                
                max_count = max(max_count, count)
        
        return max_count

# --------------- With sequence ---------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        num_set = set(nums)

        conseq_num = []

        max_count = 0

        for i in range(n):
            cur_num = nums[i]

            if cur_num - 1 not in num_set:
                count = 1
                cur_conseq_num = []

                while cur_num + 1 in num_set:
                    count += 1
                    cur_conseq_num.append(cur_num)

                    cur_num = cur_num + 1
                
                cur_conseq_num.append(cur_num) # append the last element
                if count > max_count:
                    max_count = count
                    conseq_num = cur_conseq_num[:]
        
        print(conseq_num)
        return max_count

