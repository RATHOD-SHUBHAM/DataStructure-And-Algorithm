from typing import List


class Solutions():
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if len(nums) < 3 :
            if nums[0] == nums[1]:
                return True

        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                if (abs(i - dict[nums[i]])) <= k:
                    return True
                elif(abs(i-dict[nums[i]])) > k:
                    dict[nums[i]] = i
                else:
                    return False
            else:
                dict[nums[i]] = i


def main():
    nums = [1,0,1,1]
    k = 1
    s = Solutions()
    my_func = s.containsNearbyDuplicate(nums,k)
    print(my_func)


if __name__ == '__main__':
    main()
