from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)

    idx = n - 1

    cur_sum = 0

    return recursion(idx, cur_sum, arr, k)

def recursion(idx: int, cur_sum: int, arr: List[int], k: int) -> int:
    # base case
    if idx < 0:
        if cur_sum == k:
            return 1
        else:
            return 0
        
    # Logic
    if arr[idx] <= k:
        take = recursion(idx - 1, cur_sum + arr[idx], arr, k)
    else:
        take = 0

    notTake = recursion(idx - 1, cur_sum, arr, k)
    
    return take + notTake



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 5
    print(findWays(arr, k))  # Output: 3
    arr = [1, 2, 3]
    k = 4
    print(findWays(arr, k))  # Output: 1
    arr = [1, 2, 3]
    k = 1
    print(findWays(arr, k))  # Output: 1
    arr = [1, 2, 3]
    k = -1
    print(findWays(arr, k))  # Output: 0
    arr = [1,1,4,5]
    k = 5
    print(findWays(arr, k))  # Output: 3
    arr = [1,1,1]
    k = 2
    print(findWays(arr, k))  # Output: 3
    arr = [2,34,5]
    k = 40
    print(findWays(arr, k))  # Output: 0