class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


    def partition(self, arr, left, right):
        # Consider mid to be our pivot val
        pivotIdx = left + (right - left) // 2
        pivotVal = arr[pivotIdx]

        # Place all the element smaller than this pivotVal to the left of it
        while left <= right:
            leftVal = arr[left]

            if leftVal >= pivotVal:
                self.swap(arr, left, right)
                right -= 1
            else:
                left += 1
            
        # if left is same as pivot or greater than pivot then all the elements on left of pivot is smaller than pivot
        leftVal = arr[left]   
        if leftVal < pivotVal:
            left += 1 # Pivot point is on the left
            return left # all the element on left is smaller than this val
        else:
            return left
        

    def kthSmallest(self, arr, k):
        n = len(arr)

        # Initial Hypothetical Pivot Index
        pivot_idx = n
        
        left = 0
        right = n - 1

        while pivot_idx != k:
            # get the new pivot index
            new_pivot_idx = self.partition(arr, left, right)

            if new_pivot_idx < k:
                left = new_pivot_idx
            elif new_pivot_idx > k:
                right = new_pivot_idx - 1
            else:
                # new_pivot_idx == k
                break

            pivot_idx = new_pivot_idx
        
        return arr[ : k]

if __name__ == '__main__':
    # arr = [10, 4, 5, 8, 6, 11, 26]
    # k = 3
    # arr = [10, 4, 5, 8, 6, 11, 26]
    # k = 2
    # arr = [21, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # k = 5
    # arr = [21, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # k = 2
    arr = [705478, 839185, 588573, 776836, 635764]
    k = 4
    ob = Solution()
    print(ob.kthSmallest(arr, k))