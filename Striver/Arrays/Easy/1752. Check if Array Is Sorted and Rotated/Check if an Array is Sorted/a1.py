# Using Sorted

def isSorted(arr, n) -> bool:
    return arr == sorted(arr)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    ans = isSorted(arr, n)
    print(ans)


# Using for loop

def isSorted(arr, n) -> bool:
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    ans = isSorted(arr, n)
    print(ans)