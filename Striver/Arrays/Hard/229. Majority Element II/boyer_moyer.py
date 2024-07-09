'''
    For an array of length n:

        * There can be 'at most' one majority element which is more than ⌊n/2⌋ times.
        * There can be 'at most' two majority elements which are more than ⌊n/3⌋ times.
        * There can be 'at most' three majority elements which are more than ⌊n/4⌋ times.

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count_1 = count_2 = 0
        mode_1 = mode_2 = 0
        
        for i in range(n):
            cur_num = nums[i]

            if count_1 == 0 and mode_2 != cur_num:
                mode_1 = cur_num

            if count_2 == 0 and mode_1 != cur_num:
                mode_2 = cur_num

            if mode_1 == cur_num:
                count_1 += 1
            elif mode_2 == cur_num:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1
        

        # Verify
        max_ele_1 = max_ele_2 = 0

        for num in nums:
            if num == mode_1:
                max_ele_1 += 1
            elif num == mode_2:
                max_ele_2 += 1

        maj_ele = []
        if max_ele_1 > (n // 3):
            maj_ele.append(mode_1)
        if max_ele_2 > (n // 3):
            maj_ele.append(mode_2)
        
        return maj_ele
    
# -----------------  Combined if else --------------------

'''
    For an array of length n:

        * There can be 'at most' one majority element which is more than ⌊n/2⌋ times.
        * There can be 'at most' two majority elements which are more than ⌊n/3⌋ times.
        * There can be 'at most' three majority elements which are more than ⌊n/4⌋ times.

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        count_1 = count_2 = 0
        mode_1 = mode_2 = 0
        
        for i in range(n):
            cur_num = nums[i]

            if count_1 == 0 and mode_2 != cur_num:
                mode_1 = cur_num
                count_1 += 1
            elif count_2 == 0 and mode_1 != cur_num:
                mode_2 = cur_num
                count_2 += 1
            elif mode_1 == cur_num:
                count_1 += 1
            elif mode_2 == cur_num:
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1
        

        # Verify
        max_ele_1 = max_ele_2 = 0

        for num in nums:
            if num == mode_1:
                max_ele_1 += 1
            elif num == mode_2:
                max_ele_2 += 1

        maj_ele = []
        if max_ele_1 > (n // 3):
            maj_ele.append(mode_1)
        if max_ele_2 > (n // 3):
            maj_ele.append(mode_2)
        
        return maj_ele