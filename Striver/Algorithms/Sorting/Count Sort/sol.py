class Solution:
    def count_sort(self, arr, k):
        n = len(arr)

        m = max(arr)

        count_array = [0] * (m + 1) # Storing the count of each element

        sorted_array = [0] * n

        # Step 1: Count the frequency of each element
        for i in range(n):
            idx = arr[i]
            count_array[idx] += 1
        
        # Step 2: Calculate the prefix sum, this will help us to get the index of the element in the sorted array
        for i in range(1, m + 1):
            count_array[i] += count_array[i - 1]
        
        # Step 3: Place the element in the sorted array
        for i in reversed(range(n)): # Traversing input array from end preserves the order of equal elements, , which eventually makes this sorting algorithm stable.
            countIdx = arr[i]
            sortedIdx = count_array[countIdx] - 1

            # This is done to handle the case when there are multiple elements with the same value
            count_array[countIdx] -= 1

            sorted_array[sortedIdx] = arr[i]
        
        return sorted_array


if __name__ == "__main__":
    sol = Solution()
    # arr = [1, 4, 1, 2, 7, 5, 2]
    # k = 3
    arr = [5, 17, 13, 10]
    k = 2
    sorted_array = sol.count_sort(arr, k)
    print(sorted_array)
    print(sorted_array[-k])