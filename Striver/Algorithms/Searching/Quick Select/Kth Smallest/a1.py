# ----------------------  QuickSort  ----------------------

# Time Complexity = O(nlogn)
# Space Complexity = O(logn)

# sort the array and then return the kth element from the array
def quickselect(array, k):
	helper(array,0,len(array)-1)
	return array[k-1]

def helper(array,startIdx,endIdx):
	
	if startIdx > endIdx:
		return
	
	pivot = startIdx
	left = pivot + 1
	right = endIdx
	
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array,left,right)
			
		if array[left] <= array[pivot]:
			left += 1
			
		if array[right] >= array[pivot]:
			right -= 1
			
		
	swap(array,pivot,right)
	
	smallSubarray = (right - 1) - startIdx < endIdx - (right + 1)
	
	if smallSubarray:
		helper(array,startIdx,right-1)
		helper(array,right+1,endIdx)
	else:
		helper(array,right+1,endIdx)
		helper(array,startIdx,right-1)
		
def swap(array,left,right):
	array[left],array[right] = array[right],array[left]


# ----------------------  Recursive  ----------------------

# Time complexity = O(n)
# Space Complexity = O(log)n

def quickselect(array, k):
	pos = k - 1
	helper(array,0,len(array)-1,pos)
	return array[pos]
	 
def helper(array, startIdx,endIdx,pos):
	
	if startIdx > endIdx:
		raise Exception("Error")

	pivot = startIdx
	left = pivot + 1 
	right = endIdx
	

	while left <= right:
	
		if array[left] > array[pivot] and array[right] < array[pivot]:
			swap(array,left,right)
			print(array)

		if array[left] <= array[pivot]:
			left += 1

		if array[right] >= array[pivot]:
			right -= 1
	
	swap(array, pivot, right)
	


	if right == pos:
		return
	elif right > pos:
		helper(array,startIdx,right - 1,pos)
	else:
		helper(array,right + 1,endIdx,pos)
			
def swap(array,left,right):
	array[left], array[right] = array[right],array[left]


# ----------------------  Iterative  ----------------------

# Time complexity = O(n)
# Space Complexity = O(log(n))

def quickselect(array, k):
	pos = k - 1
	return helper(array,0,len(array)-1,pos)
	 
def helper(array, startIdx,endIdx,pos):
	while True:
		if startIdx > endIdx:
			break
			
		pivot = startIdx
		left = pivot + 1 
		right = endIdx
		
		while left <= right:
			if array[left] > array[pivot] and array[right] < array[pivot]:
				swap(array,left,right)
			
			if array[left] <= array[pivot]:
				left += 1
			
			if array[right] >= array[pivot]:
				right -= 1
				
		swap(array, pivot, right)
		
		if right == pos:
			return array[pos]
		elif right > pos:
			endidx = right - 1
		else:
			startIdx = right + 1
			
def swap(array,left,right):
	array[left], array[right] = array[right],array[left]



# ----------------------  Binary  ----------------------
class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


    def partition(self, arr, left, right):
        pivotIdx = left + (right - left) // 2
        pivotVal = arr[pivotIdx]

        while left <= right:
            leftVal = arr[left]

            if leftVal >= pivotVal:
                self.swap(arr, left, right)
                right -= 1
            else:
                left += 1
            
        leftVal = arr[left]   
        if leftVal < pivotVal:
            left += 1
            return left
        else:
            return left
        

    def kthSmallest(self, arr, k):
        n = len(arr)

        # Initial Hypothetical Pivot Index
        pivot_idx = n
        
        left = 0
        right = n - 1

        while pivot_idx != k:
            new_pivot_idx = self.partition(arr, left, right)

            if new_pivot_idx < k:
                left = new_pivot_idx
            elif new_pivot_idx > k:
                right = new_pivot_idx - 1
            else:
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
    arr = [21, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    k = 2
    ob = Solution()
    print(ob.kthSmallest(arr, k))