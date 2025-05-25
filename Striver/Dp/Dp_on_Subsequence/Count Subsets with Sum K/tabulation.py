from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    n = len(arr)

    dp = [[0 for _ in range(k+1)]for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    if arr[0] == 0:
        dp[0][0] = 2
    elif arr[0] <= k:
        dp[0][arr[0]] = 1

    for idx in range(1, n):
        for cur_sum in range(k+1):
            if arr[idx] <= cur_sum:
                take = dp[idx-1][cur_sum - arr[idx]]
            else:
                take = 0

            notTake = dp[idx-1][cur_sum]
            
            dp[idx][cur_sum] = take + notTake
    
    return dp[n-1][k] % ( (10 ** 9) + 7)


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
    arr = [1,1,4,5]
    k = 5
    print(findWays(arr, k))  # Output: 3
    arr = [1,1,1]
    k = 2
    print(findWays(arr, k))  # Output: 3
    arr = [2,34,5]
    k = 40
    print(findWays(arr, k))  # Output: 0
    arr = [7 ,7 ,7 ,9 ,1 ,4 ,4 ,7 ,8 ,2, 10 ,3 ,9 ,8 ,1 ,9 ,0 ,1 ,2 ,8 ,7 ,3 ,5 ,3 ,9 ,8 ,9 ,7 ,8 ,3 ,2 ,4 ,2 ,6 ,10 ,1 ,6 ,4 ,10 ,5 ,3 ,7 ,1 ,6 ,5 ,6 ,1 ,8 ,6 ,7 ,5 ,1 ,2 ,3 ,5 ,2 ,9 ,10 ,3 ,1 ,2 ,10 ,5 ,7 ,10 ,2 ,7 ,9 ,3 ,4 ,2 ,8 ,10 ,5 ]
    k = 53
    print(findWays(arr, k))  # Output: 0
