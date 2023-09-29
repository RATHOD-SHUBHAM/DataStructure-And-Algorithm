# Tc: O(nlogn) | Sc: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        n = len(nums)

        max_sequence = -math.inf

        while i < n:
            j = i
            cur_size = 1

            cur_ele = nums[i]
            next_ele = cur_ele + 1
            # print(next_ele)

            while j+1 < n and next_ele == nums[j+1]:
                cur_size += 1

                cur_ele = next_ele
                next_ele = cur_ele + 1

                j += 1
                # print("j : ",j)
            
            max_sequence = max(max_sequence , cur_size)

            i = j + 1
            # print("i : ", i)

        return max_sequence
