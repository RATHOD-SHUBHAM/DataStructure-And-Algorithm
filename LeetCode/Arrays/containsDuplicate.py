from typing import List


class Solutions():
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = i


def main():
    nums = [1, 2, 3, 1]
    s = Solutions()
    my_func = s.containsDuplicate(nums)
    print(my_func)


if __name__ == '__main__':
    main()
