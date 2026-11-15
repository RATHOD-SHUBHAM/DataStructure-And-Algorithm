def bisect_left(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid          # keep mid as a candidate
    return left


def bisect_right(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:  # the only change: < becomes <=
            left = mid + 1
        else:
            right = mid
    return left


# LeetCode 35: works with or without duplicates
def searchInsert(nums, target):
    return bisect_left(nums, target)


# LeetCode 34: first and last occurrence
def searchRange(nums, target):
    first = bisect_left(nums, target)
    last = bisect_right(nums, target) - 1
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, last]


# Tests
a = [1, 2, 2, 2, 3]
print(bisect_left(a, 2))    # 1
print(bisect_right(a, 2))   # 4
print(searchRange(a, 2))    # [1, 3]
print(searchRange(a, 4))    # [-1, -1]

b = [1, 3, 5, 6]
print(searchInsert(b, 5))   # 2
print(searchInsert(b, 2))   # 1
print(searchInsert(b, 7))   # 4

c = [-1, 0, 3, 5, 9, 12]
print(bisect_left(c, -2), bisect_right(c, -2))   # 0 0
print(bisect_left(c, 13), bisect_right(c, 13))   # 6 6
print(bisect_left(c, 9), bisect_right(c, 9))     # 4 5