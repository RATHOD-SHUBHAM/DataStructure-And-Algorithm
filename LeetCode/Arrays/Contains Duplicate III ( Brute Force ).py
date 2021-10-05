# A Brute force approach to understand the problem statement.

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        for idx,val in enumerate(nums):
            # len(nums) = 4
            # print("idx is : ",idx)
            # [ 0 , 1 , 2 , 3 ]
            # print("val is : ",val)
            # [ 1 , 2 , 3 , 1 ]
            for j in range(idx+1 , len(nums)):
                # print(" j is : ",j)
                # [ 1 , 2 , 3 ]
                if abs(idx - j) <= k and abs(nums[idx] - nums [j]) <= t:
                    return True
        return False





def main():
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    s = Solution()
    my_func = s.containsNearbyAlmostDuplicate(nums, k, t)
    print(my_func)


if __name__ == '__main__':
    main()
